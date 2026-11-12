import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from player import Player
from query_builder import parse
from statistics import Statistics


class StubPlayerReader:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


class QueryParserTests(unittest.TestCase):
    def test_parses_team_condition(self):
        players = [
            Player("New York player", "NYR", 10, 5),
            Player("Edmonton player", "EDM", 20, 10),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(parse("team = NYR"))

        self.assertEqual([players[0]], matches)

    def test_parses_at_least_condition(self):
        players = [
            Player("Low scorer", "NYR", 9, 0),
            Player("High scorer", "NYR", 10, 0),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(parse("goals >= 10"))

        self.assertEqual([players[1]], matches)

    def test_parses_fewer_than_condition(self):
        players = [
            Player("Low scorer", "NYR", 9, 0),
            Player("High scorer", "NYR", 10, 0),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(parse("points < 10"))

        self.assertEqual([players[0]], matches)

    def test_combines_conditions_with_and(self):
        players = [
            Player("NYR low scorer", "NYR", 9, 5),
            Player("NYR high scorer", "NYR", 10, 5),
            Player("EDM high scorer", "EDM", 10, 5),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(parse("team = NYR and goals >= 10"))

        self.assertEqual([players[1]], matches)

    def test_combines_conditions_with_or(self):
        players = [
            Player("NYR player", "NYR", 1, 0),
            Player("EDM player", "EDM", 1, 0),
            Player("PHI player", "PHI", 1, 0),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(parse("team = NYR or team = EDM"))

        self.assertEqual([players[0], players[1]], matches)

    def test_and_is_evaluated_before_or(self):
        players = [
            Player("NYR low scorer", "NYR", 1, 0),
            Player("EDM low scorer", "EDM", 1, 0),
            Player("EDM high scorer", "EDM", 10, 0),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(parse("team = NYR or team = EDM and goals >= 10"))

        self.assertEqual([players[0], players[2]], matches)

    def test_negates_a_condition(self):
        players = [
            Player("NYR player", "NYR", 1, 0),
            Player("EDM player", "EDM", 1, 0),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(parse("not team = NYR"))

        self.assertEqual([players[1]], matches)

    def test_not_has_highest_precedence(self):
        players = [
            Player("NYR player", "NYR", 10, 0),
            Player("EDM player", "EDM", 1, 0),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(parse("not team = NYR or goals >= 10"))

        self.assertEqual([players[0], players[1]], matches)

    def test_rejects_malformed_queries(self):
        invalid_queries = [
            "",
            "team =",
            "team NYR",
            "goals >=",
            "goals >= many",
            "team = NYR and",
            "team = NYR or",
            "not",
            "goals = 10",
            "team >= 10",
            "team = NYR trailing",
            "TEAM = NYR",
        ]

        for query in invalid_queries:
            with self.subTest(query=query):
                with self.assertRaises(ValueError):
                    parse(query)

    def test_requires_whitespace_between_tokens(self):
        with self.assertRaises(ValueError):
            parse("team=NYR")

    def test_parses_the_phi_edm_query(self):
        players = [
            Player("PHI match", "PHI", 5, 10),
            Player("PHI goals match", "PHI", 10, 10),
            Player("EDM match", "EDM", 30, 20),
            Player("EDM points miss", "EDM", 30, 19),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(
            parse(
                "team = PHI and assists >= 10 and goals < 10 "
                "or team = EDM and points >= 50"
            )
        )

        self.assertEqual([players[0], players[2]], matches)

    def test_supports_double_negation(self):
        players = [
            Player("NYR player", "NYR", 1, 0),
            Player("EDM player", "EDM", 1, 0),
        ]
        stats = Statistics(StubPlayerReader(players))

        matches = stats.matches(parse("not not team = NYR"))

        self.assertEqual([players[0]], matches)


if __name__ == "__main__":
    unittest.main()
