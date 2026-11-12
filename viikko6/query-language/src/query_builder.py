from matchers import All, And, Not, Or, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, operations=None):
        self._operations = operations if operations else []

    def build(self):
        if not self._operations:
            return All()

        return And(*self._operations)

    # Eager evaluation subqueryille. Luin aiheesta sen verran, että pitäisi olla ihan validi
    # lähestymistapa (Eager vs. lazy "hyvyys" riippuu käyttötapauksesta).
    # En löytänyt tehtävänannosta tai materiaalista mainintaa pitäisikö "subqueryt" instantioida
    # build stepissä, kuten pääoperaatio, vai jo aiemmin

    def plays_in(self, team: str):
        return QueryBuilder([*self._operations, PlaysIn(team)])

    def has_at_least(self, value: int, attr: str):
        return QueryBuilder([*self._operations, HasAtLeast(value, attr)])

    def has_fewer_than(self, value: int, attr: str):
        return QueryBuilder([*self._operations, HasFewerThan(value, attr)])

    def one_of(self, *queries):
        return QueryBuilder([Or(*(q.build() for q in queries))])


class _QueryParser:
    def __init__(self, query):
        self._tokens = query.split()
        self._position = 0

    def parse(self):
        if not self._tokens:
            raise ValueError("Invalid query")

        matcher = self._parse_or()

        if self._position != len(self._tokens):
            raise ValueError("Invalid query")

        return matcher

    def _parse_or(self):
        matchers = [self._parse_and()]

        while self._accept("or"):
            matchers.append(self._parse_and())

        return matchers[0] if len(matchers) == 1 else Or(*matchers)

    def _parse_and(self):
        matchers = [self._parse_not()]

        while self._accept("and"):
            matchers.append(self._parse_not())

        return matchers[0] if len(matchers) == 1 else And(*matchers)

    def _parse_not(self):
        if self._accept("not"):
            return Not(self._parse_not())

        return self._parse_condition()

    def _parse_condition(self):
        if self._position + 2 >= len(self._tokens):
            raise ValueError("Invalid query")

        attribute = self._tokens[self._position]
        operator = self._tokens[self._position + 1]
        value = self._tokens[self._position + 2]
        self._position += 3

        if attribute == "team" and operator == "=" and value.isidentifier():
            return QueryBuilder().plays_in(value).build()

        if attribute not in ("goals", "assists", "points"):
            raise ValueError("Invalid query")

        try:
            integer = int(value)
        except ValueError as error:
            raise ValueError("Invalid query") from error

        if operator == ">=":
            return QueryBuilder().has_at_least(integer, attribute).build()

        if operator == "<":
            return QueryBuilder().has_fewer_than(integer, attribute).build()

        raise ValueError("Invalid query")

    def _accept(self, token):
        if self._position < len(self._tokens) and self._tokens[self._position] == token:
            self._position += 1
            return True

        return False


def parse(query):
    return _QueryParser(query).parse()
