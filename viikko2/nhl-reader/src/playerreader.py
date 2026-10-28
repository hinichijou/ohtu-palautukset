import requests
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        response = requests.get(url).json()
        self.__players = [Player(p) for p in response]
        self._nationalities = {p.nationality for p in self.__players}

    def get_players(self):
        return self.__players

    def get_nationalities(self):
        return self._nationalities
