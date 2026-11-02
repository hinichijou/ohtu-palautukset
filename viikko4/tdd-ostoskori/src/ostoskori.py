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
        for ostos in self._ostokset:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        self._tavaroiden_maara -= 1
        self._hinta -= poistettava.hinta()
        self._ostokset[0].muuta_lukumaaraa(-1)
        if self._ostokset[0].lukumaara() == 0:
            self._ostokset.pop(0)

    def tyhjenna(self):
        self._tavaroiden_maara = 0
        self._hinta = 0
        self._ostokset = []

    def ostokset(self):
        return self._ostokset
