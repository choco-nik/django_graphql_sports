import graphene
from graphene_django.types import DjangoObjectType
from .models import League, Team, Match, Result

class LeagueType(DjangoObjectType):
    class Meta:
        model = League

class TeamType(DjangoObjectType):
    class Meta:
        model = Team

class MatchType(DjangoObjectType):
    class Meta:
        model = Match

class ResultType(DjangoObjectType):
    class Meta:
        model = Result

class Query(graphene.ObjectType):
    leagues = graphene.List(LeagueType)
    teams = graphene.List(TeamType)
    matches = graphene.List(MatchType)
    results = graphene.List(ResultType)

    def resolve_leagues(self, info):
        return League.objects.all()

    def resolve_teams(self, info):
        return Team.objects.all()

    def resolve_matches(self, info):
        return Match.objects.all()

    def resolve_results(self, info):
        return Result.objects.all()

schema = graphene.Schema(query=Query)
