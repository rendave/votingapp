from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max,Count


class Position(models.Model):
    position_name = models.CharField(max_length=200)
    maximum_candidates = models.IntegerField(default=3)

    def is_voted(self, voter):
        return voter.votes.filter(candidate__position=self).exists()

    def __str__(self):
        return self.position_name

    def get_winner(self):
        return Candidate.objects.filter(
            position=self).annotate(
            num_votes=Count('votes')).order_by("-num_votes").first()


class Party(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, blank=True, null=True)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "{} for {}".format(
            self.owner.get_full_name(),
            self.position.position_name)

    def is_voted(self, voter):
        # return voter.votes.filter(owner=voter).exists()
        return self.votes.filter(owner=voter).exists()

    def add_vote(self, voter):
        if (
                not self.is_voted(voter) and
                not self.position.is_voted(voter)):
            Vote.objects.create(owner=voter, candidate=self)

    def unvote(self, voter):
        Vote.objects.filter(owner=voter, candidate=self).delete()

    @property
    def vote_count(self):
        return self.votes.count()


class Vote(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="votes")
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="votes")
