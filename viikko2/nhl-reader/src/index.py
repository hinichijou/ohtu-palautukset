from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from seasonsreader import SeasonsReader
from playerreader import PlayerReader
from playerstats import PlayerStats

def prompt_seasons():
    seasons_url = "https://studies.cs.helsinki.fi/nhlstats"
    seasonsreader = SeasonsReader(seasons_url)
    season = Prompt.ask("Season", choices=seasonsreader.seasons, default="2024-25")

    return season

def get_stats(season: str):
    players_url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    playerreader = PlayerReader(players_url)
    stats = PlayerStats(playerreader)

    return stats

def print_table(console: Console, players: list, season: str, group: str):
    table = Table(title=f"Season {season} players from {group}:")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    for p in players:
        table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))

    console.print(table)


def get_players(stats: PlayerStats):
    search_type = Prompt.ask(
        "Search players by", choices=["nationality", "team"]
    )

    if search_type == "nationality":
        group = Prompt.ask("Nationality", choices=stats.get_nationalities())
        players = stats.top_scorers_by_nationality(group)
    else:
        group = Prompt.ask("Team", choices=stats.get_teams())
        players = stats.top_scorers_by_team(group)

    return group, players


def main():
    console = Console()

    season = prompt_seasons()
    stats = get_stats(season)

    while True:
        group, players = get_players(stats)
        print_table(console, players, season, group)

if __name__ == "__main__":
    main()
