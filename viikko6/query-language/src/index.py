from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

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

    print()

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    print_matches(stats, matcher)

    print()

    matcher = And(
    HasAtLeast(70, "points"),
        Or(
            PlaysIn("COL"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    print_matches(stats, matcher)


if __name__ == "__main__":
    main()
