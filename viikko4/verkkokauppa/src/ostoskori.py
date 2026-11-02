class Ostoskori:
    def __init__(self):
        self._tuotteet = []

    def lisaa(self, tuote):
        self._tuotteet.append(tuote)

    def poista(self, tuote):
        # Tehtävä 5: sen perusteella miten ostoskoriin voidaan lisätä useampi sama tuote
        # ja miten varaston palauta_varastoon on toteutettu, voidaan päätellä, että kaikkien
        # saman id:n tuotteiden poistaminen on bugi. Poistetaan vain yksi.
        self._tuotteet.remove(tuote)

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
