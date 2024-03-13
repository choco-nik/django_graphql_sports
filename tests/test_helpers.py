import responses
import pytest
from django_graphql_sports.app.helpers import (
    NoDataReturned,
    get_football_games,
    get_nba_games,
)
from django_graphql_sports.config import AppConfig


@pytest.fixture
def config():
    return AppConfig(
        FOOTBALL_URL="https://example.com",
        FOOTBALL_API_KEY="your-api-key",
        BASKETBALL_URL="https://example.com",
        BASKETBALL_API_KEY="your-api-key",
    )


@responses.activate
def test_get_football_game_no_data(config: AppConfig):
    competition_id = 123

    responses.add(
        responses.GET,
        url=(f"{config.FOOTBALL_URL}/v4/competitions/{competition_id}/matches"),
        json={
            "matches": [],
        },
        status=200,
    )

    with pytest.raises(NoDataReturned):
        get_football_games(config, competition_id)


@responses.activate
def test_get_football_game_successful(config: AppConfig):
    competition_id = 123

    sample_matches = [
        {
            "id": 1,
            "home_team": "Team A",
            "away_team": "Team B",
            "utcDate": "2023-01-01T12:00:00Z",
            "status": "FINISHED",
            "score": {"fullTime": {"home": 1, "away": 0}},
        },
        {
            "id": 2,
            "home_team": "Team C",
            "away_team": "Team D",
            "utcDate": "2023-01-02T12:00:00Z",
            "status": "FINISHED",
            "score": {"fullTime": {"home": 2, "away": 1}},
        },
    ]

    responses.add(
        responses.GET,
        url=(f"{config.FOOTBALL_URL}/v4/competitions/{competition_id}/matches"),
        json={
            "matches": sample_matches,
        },
        status=200,
    )

    result = get_football_games(config, competition_id)

    assert len(result) == len(sample_matches)


@responses.activate
def test_get_basketball_game_no_data(config: AppConfig):

    responses.add(
        responses.GET,
        url=(f"{config.BASKETBALL_URL}/v1/games"),
        json={
            "data": [],
        },
        status=200,
    )

    with pytest.raises(NoDataReturned):
        get_nba_games(config)


@responses.activate
def test_get_nba_games(config: AppConfig):
    responses.add(
        responses.GET,
        url=f"{config.BASKETBALL_URL}/v1/games",
        json={"data": []},
        status=200,
    )

    with pytest.raises(NoDataReturned):
        get_nba_games(config)

    responses.replace(
        responses.GET,
        url=f"{config.BASKETBALL_URL}/v1/games",
        json={
            "data": [
                {
                    "date": "2018-10-16",
                    "status": "Final",
                    "home_team_score": 105,
                    "visitor_team_score": 87,
                    "home_team": {
                        "full_name": "Boston Celtics",
                    },
                    "visitor_team": {
                        "full_name": "Philadelphia 76ers",
                    },
                }
            ]
        },
        status=200,
    )

    result = get_nba_games(config)
    assert len(result) == 1
    assert result[0]["date"] == "2018-10-16"
