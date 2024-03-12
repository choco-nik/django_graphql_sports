import requests

def get_football_games(competition_id, page=1, page_size=40):
    url = f"https://api.football-data.org/v4/competitions/{competition_id}/matches"
    headers = {"X-Auth-Token": "ea32770561614c50b01e46b75c957eee"}
    params = {"page": page, "page_size": page_size}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['matches']
    else:
        return []
    
# def get_nba_games():
#     url = "http://api.balldontlie.io/v1/games"
#     headers = {"Authorization": "b2a89977-91d6-4f8b-9075-583f7fe20edc"}  #the api key shouldn't be here 
#     params={"per_page": 40}

#     response = requests.get(url, headers=headers, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         return data
#     else:
#         return None, None

def get_paginated_players(page=1, per_page=25):
    all_players = []
    url = "http://api.balldontlie.io/v1/games"
    headers = {"Authorization": "b2a89977-91d6-4f8b-9075-583f7fe20edc"}  #the api key shouldn't be here 
    params = {"page": page, "per_page": per_page}
    
    while True:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if not data["data"]:
            break
        all_players.extend(data["data"])
        
        # Update pagination params for the next page
        next_cursor = data["meta"]["next_cursor"]
        params["page"] = next_cursor
    
    return all_players
