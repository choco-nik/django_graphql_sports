import requests
from django_graphql_sports.config import AppConfig

class NoDataReturned(Exception):
    pass

def get_football_games(config: AppConfig, competition_id):
    url = f"{config.FOOTBALL_URL}/v4/competitions/{competition_id}/matches"
    headers = {"X-Auth-Token": config.FOOTBALL_API_KEY}
    try:
        response = requests.get(url, headers=headers)
        matches = response.json()['matches']
        if len(matches) == 0:
            NoDataReturned()
        return sorted(matches, key=lambda d: d['utcDate'], reverse=True)
    except Exception:
        raise

def get_nba_games(config: AppConfig = None):
    url = f"{config.BASKETBALL_URL}/v1/games"
    headers = {"Authorization": config.BASKETBALL_API_KEY}
    params={"per_page": 40}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if len(data) == 0:
            NoDataReturned()
        return data
    else:
        raise Exception