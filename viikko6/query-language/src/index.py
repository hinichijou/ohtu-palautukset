from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder, parse
from matchers import And


def print_matches(stats, matcher):
    for player in stats.matches(matcher):
        print(player)

    print()

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    # Print all players
    matcher = query.build()
    print_matches(stats, matcher)

    # Print all players from NYR
    matcher = query.plays_in("NYR").build()
    print_matches(stats, matcher)

    # Print all players from NYR with at least 10 and less than 20 goals
    matcher = query.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()
    print_matches(stats, matcher)

    # Print all players from PHI with at least 10 assists and less than 10 goals and
    # players with more than 50 points from EDM
    matcher = (
        query.one_of(
            query.plays_in("PHI")
                .has_at_least(10, "assists")
                .has_fewer_than(10, "goals"),
            query.plays_in("EDM")
                .has_at_least(50, "points")
        ).build()
    )
    print_matches(stats, matcher)

    # Print all players from NYR with at least 10 and less than 20 goals parsing a string query
    matcher = parse("team = NYR and goals >= 10 and goals < 20")
    print_matches(stats, matcher)

    # Print all players from PHI with at least 10 assists and less than 10 goals and
    # players with more than 50 points from EDM parsing a string query
    matcher = parse("team = PHI and assists >= 10 and goals < 10 or team = EDM and points >= 50")
    print_matches(stats, matcher)

    matcher = parse("points = 50")
    print_matches(stats, matcher)

if __name__ == "__main__":
    main()
