from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.__reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = [p for p in self.__reader.get_players() if p.nationality == "FIN"]
        players.sort(key = lambda p: p.points, reverse = True)
        return players