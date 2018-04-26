
from django import template
register = template.Library()


@register.filter
def is_voted_candidate(candidate, voter):
    return candidate.is_voted(voter)


@register.filter
def is_voted_position(position, voter):
    return position.is_voted(voter)
