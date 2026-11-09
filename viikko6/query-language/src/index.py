from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All

def print_matches(stats, matcher):
    for player in stats.matches(matcher):
        print(player)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    print_matches(stats, matcher)

    print()

    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    print_matches(stats, matcher)

    print()

    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    print_matches(stats, matcher)

    print()

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


if __name__ == "__main__":
    main()
