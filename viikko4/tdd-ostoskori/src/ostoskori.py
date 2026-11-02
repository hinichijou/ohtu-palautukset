from tuote import Tuote

class Ostoskori:
    def __init__(self):
        self._tavaroiden_maara = 0
        self._hinta = 0

    def tavaroita_korissa(self):
        return self._tavaroiden_maara

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self._tavaroiden_maara += 1
        self._hinta = lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        pass

    def tyhjenna(self):
        pass

    def ostokset(self):
        pass
