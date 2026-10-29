import requests
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        #Add timeout handling if necessary
        response = requests.get(url, timeout=10).json()
        self.__players = [Player(p) for p in response]

    def get_players(self):
        return self.__players

    def __str__(self):
        return "\n".join([str(p) for p in self.__players])
