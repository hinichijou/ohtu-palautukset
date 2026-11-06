from abc import ABC, abstractmethod
class BinaariOperaatio(ABC):
    def __init__(self, sovelluslogiikka, lue_syote):
        self.lue_syote = lue_syote
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        arvo = 0

        try:
            arvo = int(self.lue_syote())
        except Exception:
            pass

        self.laske(arvo)

    @abstractmethod
    def laske(self, arvo: int):
        pass

class Summa(BinaariOperaatio):
    def laske(self, arvo: int):
        self.sovelluslogiikka.plus(arvo)

class Erotus(BinaariOperaatio):
    def laske(self, arvo: int):
        self.sovelluslogiikka.miinus(arvo)

class Nollaus(BinaariOperaatio):
    def laske(self, arvo: int):
        self.sovelluslogiikka.nollaa()

class Kumoa(BinaariOperaatio):
    # Tehtävä 6.1: Tässä tehtävässä ei tarvitse vielä toteuttaa kumoa-komennon toiminnallisuutta!
    def laske(self, arvo: int):
        pass