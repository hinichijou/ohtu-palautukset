from abc import ABC, abstractmethod

class All:
    def test(self, _):
        return True

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        return all(m.test(player) for m in self._matchers)

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        return any(m.test(player) for m in self._matchers)

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)

class PlayerHasOperation(ABC):
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return self.evaluate(player_value)

    @abstractmethod
    def evaluate(self, player_value):
        pass

class HasAtLeast(PlayerHasOperation):
    def evaluate(self, player_value):
        return player_value >= self._value

class HasFewerThan(PlayerHasOperation):
    def evaluate(self, player_value):
        return player_value < self._value

class HasExactly(PlayerHasOperation):
    def evaluate(self, player_value):
        return player_value == self._value

class PlaysIn(HasExactly):
    def __init__(self, team):
        super().__init__(team, "team")
