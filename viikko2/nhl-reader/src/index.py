from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from seasonsreader import SeasonsReader
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    console = Console()

    seasons_url = "https://studies.cs.helsinki.fi/nhlstats"
    seasonsreader = SeasonsReader(seasons_url)
    season = Prompt.ask("Season", choices=seasonsreader.seasons, default="2024-25")

    players_url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    playerreader = PlayerReader(players_url)
    stats = PlayerStats(playerreader)

    while True:
        nationality = Prompt.ask("Nationality", choices=playerreader.get_nationalities())
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Season {season} players from {nationality}:")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        for p in players:
            table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))

        console.print(table)

if __name__ == "__main__":
    main()
