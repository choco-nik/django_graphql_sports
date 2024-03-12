import responses
import pytest
from django_graphql_sports.app import helpers
from django_graphql_sports.config import AppConfig

@pytest.fixture
def config():
    return AppConfig(
        FOOTBALL_URL="https://example.com",
        FOOTBALL_API_KEY="your-api-key"
    )

@responses.activate
def test_get_football_game(config: AppConfig):
    competition_id = 123

    responses.add(
        responses.GET,
        url=(f"{config.FOOTBALL_URL}/v4/competitions/{competition_id}/matches"),
        json={
            "matches": [],
        },
        status=200,
    )

    with pytest.raises(helpers.NoDataReturned):
        result = helpers.get_football_games(config, competition_id)

    assert len(result) == 0