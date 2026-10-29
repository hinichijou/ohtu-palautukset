import pytest
import requests

from player import Player
from playerstats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self.__players = players

    def get_players(self):
        return self.__players


@pytest.fixture(autouse=True)
def no_http_requests(monkeypatch):
    def fail_if_called(*args, **kwargs):
        raise AssertionError("Tests must not make HTTP requests")

    monkeypatch.setattr(requests, "get", fail_if_called)


@pytest.fixture
def stats():
    players = [
        Player({
            "name": "Player One",
            "nationality": "FIN",
            "assists": 10,
            "goals": 20,
            "team": "Team A",
        }),
        Player({
            "name": "Player Two",
            "nationality": "FIN",
            "assists": 30,
            "goals": 5,
            "team": "Team A",
        }),
        Player({
            "name": "Player Three",
            "nationality": "SWE",
            "assists": 15,
            "goals": 15,
            "team": "Team B",
        }),
        Player({
            "name": "Player Four",
            "nationality": "SWE",
            "assists": 2,
            "goals": 3,
            "team": "Team A, Team B",
        }),
    ]
    return PlayerStats(PlayerReaderStub(players))


def test_http_requests_are_blocked():
    with pytest.raises(AssertionError, match="Tests must not make HTTP requests"):
        requests.get("https://example.com")


def test_top_scorers_by_nationality_returns_players_by_points(stats):
    players = stats.top_scorers_by_nationality("FIN")

    assert [player.name for player in players] == ["Player Two", "Player One"]


def test_top_goal_scorers_returns_requested_number(stats):
    players = stats.top_goal_scorers(2)

    assert [player.name for player in players] == ["Player One", "Player Three"]


def test_get_nationalities_returns_all_nationalities(stats):
    assert stats.get_nationalities() == {"FIN", "SWE"}


def test_top_scorers_by_team_returns_players_by_points(stats):
    players = stats.top_scorers_by_team("Team A")

    assert [player.name for player in players] == [
        "Player Two", "Player One", "Player Four"
    ]


def test_player_who_played_for_two_teams_is_found_for_both_teams(stats):
    team_b_players = stats.top_scorers_by_team("Team B")

    assert "Player Four" in [player.name for player in team_b_players]


def test_get_teams_returns_all_teams(stats):
    assert stats.get_teams() == {"Team A", "Team B"}
