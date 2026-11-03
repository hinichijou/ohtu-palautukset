class Player:
    def __init__(self, name: str):
        self.__name = name
        self.__score = 0

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    def increment_score(self):
        self.__score = self.__score + 1

    def reset_score(self):
        self.__score = 0