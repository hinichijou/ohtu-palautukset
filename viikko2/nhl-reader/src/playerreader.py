import requests
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        self.__url = url
        self.__players = []

    def get_players(self):
        if len(self.__players) == 0:
            response = requests.get(self.__url).json()
            self.__players = [Player(p) for p in response]

        return self.__players
