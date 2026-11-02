from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._tavaroiden_maara = 0
        self._hinta = 0
        self._ostokset = []

    def tavaroita_korissa(self):
        return self._tavaroiden_maara

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self._tavaroiden_maara += 1
        self._hinta += lisattava.hinta()
        if self._ostokset and self._ostokset[0].tuote == lisattava:
            self._ostokset[0].muuta_lukumaaraa(1)
            return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        self._tavaroiden_maara -= 1
        self._hinta -= poistettava.hinta()
        self._ostokset[0].muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass

    def ostokset(self):
        return self._ostokset
