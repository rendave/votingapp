from django.shortcuts import render, get_object_or_404
from .models import Candidate, Position, Vote, Party


def home(request):
    position_list = Position.objects.all()
    return render(
        request,
        'votingapp/home.html',
        {'user': request.user, 'position_list': position_list})


def login(request):
    return render(
        request,
        'votingapp/login.html')


def position_page(request):
    position_list = Position.objects.all()
    return render(
        request,
        'votingapp/position_page.html',
        {'position_list': position_list})


def vote_position_page(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    candidate_list = Candidate.objects.filter(position=position)
    vote = Vote.objects.filter(
        owner=request.user, candidate__position=position)
    # true or false
    status = vote.exists()
    print(status)
    return render(
        request, 'votingapp/vote_position.html',
        {
            'position': position,
            'candidate_list': candidate_list,
            'status': status,
            'user': request.user})


def vote_position_post(request, position_id, candidate_id):
    # get candidate
    candidate = Candidate.objects.get(pk=candidate_id)
    print(candidate)
    print("wrong function")
    candidate.add_vote(request.user)
    return position_page(request)


def party_page(request):
    party_list = Party.objects.all()
    return render(
        request, 'votingapp/party_page.html',
        {'party_list': party_list})


def vote_party_page(request, party_id):
    # unfinished
    party = get_object_or_404(Party, pk=party_id)
    candidate_list = Candidate.objects.filter(
        party=party_id).order_by()
    return render(
        request,
        'votingapp/vote_candidate_page.html',
        {
            'candidate_list': candidate_list, 'party': party,
            'curr_user': request.user})


def vote_party_post(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    for candidate in party.candidate_set.all():
        candidate.add_vote(request.user)
    return vote_party_page(request, party.id)


def unvote_position_post(request, position_id, candidate_id):
    # get candidate
    candidate = Candidate.objects.get(pk=candidate_id)
    candidate.unvote(request.user)
    print("right function")
    return position_page(request)
