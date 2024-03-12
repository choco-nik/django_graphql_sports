from .models import Competition, Match

def resolve_competitions(info):
    return Competition.objects.all()

def resolve_matches(info):
    return Match.objects.all()
