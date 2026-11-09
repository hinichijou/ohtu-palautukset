from matchers import All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, create_query=All, operations=None):
        self._create_query = create_query
        self._operations = operations if operations else []

    def build(self):
        return self._create_query(*self._operations)

    def plays_in(self, team: str):
        return QueryBuilder(self._create_query, [*self._operations, PlaysIn(team)])

    def has_at_least(self, value: int, attr: str):
        return QueryBuilder(self._create_query, [*self._operations, HasAtLeast(value, attr)])

    def has_fewer_than(self, value: int, attr: str):
        return QueryBuilder(self._create_query, [*self._operations, HasFewerThan(value, attr)])
