from matchers import All, And, Or, PlaysIn, HasAtLeast, HasFewerThan

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
