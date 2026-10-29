from re import search
import requests

class SeasonsReader:
    def __init__(self, url: str):
        #Add timeout handling if necessary
        resp = requests.get(url, timeout=10)
        seasons_str = search(">following seasons available  (.*)<", resp.text).group(1)
        self.__seasons = seasons_str.split(", ")

    @property
    def seasons(self):
        return self.__seasons

    def __str__(self):
        return ", ".join(self.__seasons)
