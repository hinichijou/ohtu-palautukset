from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.__reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = [p for p in self.__reader.get_players() if p.nationality == nationality]
        players.sort(key = lambda p: p.points, reverse = True)
        return players

    def top_scorers_by_team(self, team: str):
        players = [
            p for p in self.__reader.get_players()
            if team in self._get_player_teams(p)
        ]
        players.sort(key = lambda p: p.points, reverse = True)
        return players

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        players = self.__reader.get_players()
        players.sort(key = lambda p: p.goals, reverse = True)
        return players[:how_many]

    def get_nationalities(self):
        return {p.nationality for p in self.__reader.get_players()}

    def get_teams(self):
        return {
            team
            for player in self.__reader.get_players()
            for team in self._get_player_teams(player)
        }

    def _get_player_teams(self, player):
        return set(player.team.split(", "))
