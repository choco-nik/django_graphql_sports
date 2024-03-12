from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_graphql_sports.app.helpers import get_football_games, get_nba_games
from django_graphql_sports.config import get_config



def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def football(request):
    config = get_config()

    competition_id = 2003
    try:
      matches = get_football_games(config, competition_id)
      paginator = Paginator(matches, 40)
      page_number = request.GET.get('page')
      try:
          page_matches = paginator.page(page_number)
      except PageNotAnInteger:
          page_matches = paginator.page(1)
      except EmptyPage:
          page_matches = paginator.page(paginator.num_pages)
      
      return render(request, 'football.html', {'page_matches': page_matches})
    
    except Exception:
        return render(request, 'error.html')
 

def basketball(request):
    config = get_config()

    try:
      matches = get_nba_games(config)
      paginator = Paginator(matches, 40)
      page_number = request.GET.get('page')
      try:
          page_matches = paginator.page(page_number)
      except PageNotAnInteger:
          page_matches = paginator.page(1)
      except EmptyPage:
          page_matches = paginator.page(paginator.num_pages)
      
      return render(request, 'basketball.html', {'page_matches': page_matches})
    
    except Exception:
        return render(request, 'error.html')