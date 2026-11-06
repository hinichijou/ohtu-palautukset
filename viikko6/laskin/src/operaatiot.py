from abc import ABC, abstractmethod
class Operaatio(ABC):
    def __init__(self, sovelluslogiikka, lue_syote):
        self.__lue_syote = lue_syote
        self._sovelluslogiikka = sovelluslogiikka
        self._arvo = 0
        # 6.2: Komento-olion tulee siis muistaa, mikä oli tuloksen arvo ennen komennon suoritusta,
        # jotta se osaa palauttaa laskimen suoritusta edeltävään tilaan.
        self._edeltavat_arvot = []

    def _lue_arvo(self):
        try:
            self._arvo = int(self.__lue_syote())
        except Exception:
            return False

        return True

    def suorita(self):
        edellinen_arvo = self._sovelluslogiikka.arvo()
        tallenna = self._operaatio()

        if tallenna:
            self._edeltavat_arvot.append(edellinen_arvo)

        return tallenna

    @abstractmethod
    def _operaatio(self):
        pass

    # 6.2: Periaatteena on toteuttaa jokaiseen komento-olioon metodi kumoa
    def kumoa(self):
        if len(self._edeltavat_arvot) > 0:
            self._sovelluslogiikka.aseta_arvo(self._edeltavat_arvot.pop())

class Summa(Operaatio):
    def _operaatio(self):
        if not self._lue_arvo():
            return False

        self._sovelluslogiikka.plus(self._arvo)

        return True

class Erotus(Operaatio):
    def _operaatio(self):
        if not self._lue_arvo():
            return False

        self._sovelluslogiikka.miinus(self._arvo)

        return True

class Nollaus(Operaatio):
    def _operaatio(self):
        self._sovelluslogiikka.nollaa()
        return True
