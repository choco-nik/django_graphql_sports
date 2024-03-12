import requests

def get_competition_standings(competition_id, page=1, page_size=40):
    url = f"https://api.football-data.org/v4/competitions/{competition_id}/matches"
    headers = {"X-Auth-Token": "ea32770561614c50b01e46b75c957eee"}
    params = {"page": page, "page_size": page_size}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['matches']
    else:
        # Throw an Error perhaps
        return []
    


def get_nba_games(page=1, per_page=40):
    url = "http://api.balldontlie.io/v1/games"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    params = {"page": page, "per_page": per_page, "sort": "date"}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        # Think how to handle an empty response
        return None
