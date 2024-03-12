import requests

def get_football_games(competition_id):
    url = f"https://api.football-data.org/v4/competitions/{competition_id}/matches?"
    headers = {"X-Auth-Token": "ea32770561614c50b01e46b75c957eee"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['matches']
    
    else:
        return []
    
def get_nba_games():
    url = "http://api.balldontlie.io/v1/games"
    headers = {"Authorization": "b2a89977-91d6-4f8b-9075-583f7fe20edc"}  #the api key shouldn't be here 
    params={"per_page": 40}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None, None
