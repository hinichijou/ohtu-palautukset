import requests
from re import search

class SeasonsReader:
    def __init__(self, url: str):
        resp = requests.get(url)
        seasons_str = search(">following seasons available  (.*)<", resp.text).group(1)
        self.__seasons = seasons_str.split(", ")

    @property
    def seasons(self):
        return self.__seasons
