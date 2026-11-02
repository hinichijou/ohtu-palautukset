from tuote import Tuote

class Ostoskori:
    def __init__(self):
        self._tuote_lisatty = False
        self._hinta = 0

    def tavaroita_korissa(self):
        return 1 if self._tuote_lisatty else 0

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self._tuote_lisatty = True
        self._hinta = lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        pass

    def tyhjenna(self):
        pass

    def ostokset(self):
        pass
