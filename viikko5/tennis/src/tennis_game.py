from enum import IntEnum

from player import Player

class Score(IntEnum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.__player1 = Player(player1_name)
        self.__player2 = Player(player2_name)

    def won_point(self, player_name):
        if self.__player1.name == player_name:
            self.__player1.increment_score()
        else:
            self.__player2.increment_score()

    def get_tie_str(self):
        if self.__player1.score < Score.Forty:
            return f"{Score(self.__player1.score).name}-All"

        return "Deuce"

    def get_advantage_str(self):
        leading_player = max(self.__player1, self.__player2, key=lambda p: p.score)
        difference = abs(self.__player1.score - self.__player2.score)
        return (
            f"Advantage {leading_player.name}" if difference == 1
            else f"Win for {leading_player.name}"
        )

    def get_score_str(self):
        return f"{Score(self.__player1.score).name}-{Score(self.__player2.score).name}"

    def get_score(self):
        # Special case: tie game. Either -All suffix or Deuce
        if self.__player1.score == self.__player2.score:
            return self.get_tie_str()

        # Special case: advantage. Either player has the advantage or has won the game.
        if self.__player1.score > Score.Forty or self.__player2.score > Score.Forty:
            return self.get_advantage_str()

        return self.get_score_str()
