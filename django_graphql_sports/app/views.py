from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django_graphql_sports.app.helpers import get_football_games

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def football(request):
    competition_id = 2003
    matches = get_football_games(competition_id)
    return render(request, 'football.html', {'matches': matches})

def basketball(request):
  template = loader.get_template('basketball.html')
  return HttpResponse(template.render())