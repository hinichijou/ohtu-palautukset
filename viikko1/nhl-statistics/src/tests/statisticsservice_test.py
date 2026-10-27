import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_pelaajat_loytyy_nimella(self):
        self.assertEqual(str(self.stats.search("Semenko")), str(Player("Semenko", "EDM", 4, 12)))
        self.assertEqual(str(self.stats.search("Lemieux")), str(Player("Lemieux", "PIT", 45, 54)))
        self.assertEqual(str(self.stats.search("Kurri")), str(Player("Kurri",   "EDM", 37, 53)))
        self.assertEqual(str(self.stats.search("Yzerman")), str(Player("Yzerman", "DET", 42, 56)))
        self.assertEqual(str(self.stats.search("Gretzky")), str(Player("Gretzky", "EDM", 35, 89)))

    def test_tuntematon_pelaaja_palauttaa_null(self):
        self.assertIsNone(self.stats.search("AnhYzerman"))

    def test_joukkueen_pelaajien_haku(self):
        joukkueen_pelaajat = self.stats.team("EDM")
        self.assertEqual(len(joukkueen_pelaajat), 3)
        self.assertIsNotNone(next((p for p in joukkueen_pelaajat if p.name == "Semenko"), None))
        self.assertIsNotNone(next((p for p in joukkueen_pelaajat if p.name == "Kurri"), None))
        self.assertIsNotNone(next((p for p in joukkueen_pelaajat if p.name == "Gretzky"), None))

    def test_tuntemattoman_joukkueen_pelaajien_haku_palauttaa_tyhjan_listan(self):
        joukkueen_pelaajat = self.stats.team("Edmonton Hurricanes")
        self.assertEqual(joukkueen_pelaajat, [])

    def test_top_neg_palauttaa_tyhjan_listan(self):
        eniten_pisteita_tehneet_pelaajat = self.stats.top(-1)
        self.assertEqual(eniten_pisteita_tehneet_pelaajat, [])

    def test_top_nolla_palauttaa_yhden_pelaajan(self):
        eniten_pisteita_tehneet_pelaajat = self.stats.top(0)
        self.assertEqual(len(eniten_pisteita_tehneet_pelaajat), 1)

    def test_top_kymmenen_palauttaa_list_out_of_range(self):
        with self.assertRaises(IndexError):
            self.stats.top(10)

    def test_viiden_eniten_pisteita_tehneen_pelaajan_haku(self):
        eniten_pisteita_tehneet_pelaajat = self.stats.top(4)
        self.assertEqual(len(eniten_pisteita_tehneet_pelaajat), 5)

        self.assertEqual(str(eniten_pisteita_tehneet_pelaajat[0]), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertEqual(str(eniten_pisteita_tehneet_pelaajat[1]), str(Player("Lemieux", "PIT", 45, 54)))
        self.assertEqual(str(eniten_pisteita_tehneet_pelaajat[2]), str(Player("Yzerman", "DET", 42, 56)))
        self.assertEqual(str(eniten_pisteita_tehneet_pelaajat[3]), str(Player("Kurri",   "EDM", 37, 53)))
        self.assertEqual(str(eniten_pisteita_tehneet_pelaajat[4]), str(Player("Semenko", "EDM", 4, 12)))

    def test_kahden_eniten_pisteita_tehneen_pelaajan_haku(self):
        eniten_pisteita_tehneet_pelaajat = self.stats.top(1)
        self.assertEqual(len(eniten_pisteita_tehneet_pelaajat), 2)

        self.assertEqual(str(eniten_pisteita_tehneet_pelaajat[0]), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertEqual(str(eniten_pisteita_tehneet_pelaajat[1]), str(Player("Lemieux", "PIT", 45, 54)))

        # Testi eksplisiittisellä parametrilla
        eniten_pisteita_tehneet_pelaajat = self.stats.top(1, SortBy.POINTS)
        self.assertEqual(len(eniten_pisteita_tehneet_pelaajat), 2)

        self.assertEqual(str(eniten_pisteita_tehneet_pelaajat[0]), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertEqual(str(eniten_pisteita_tehneet_pelaajat[1]), str(Player("Lemieux", "PIT", 45, 54)))


    def test_kolmen_eniten_maaleja_tehneen_pelaajan_haku(self):
        eniten_maaleja_tehneet_pelaajat = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(len(eniten_maaleja_tehneet_pelaajat), 3)

        self.assertEqual(str(eniten_maaleja_tehneet_pelaajat[0]), str(Player("Lemieux", "PIT", 45, 54)))
        self.assertEqual(str(eniten_maaleja_tehneet_pelaajat[1]), str(Player("Yzerman", "DET", 42, 56)))
        self.assertEqual(str(eniten_maaleja_tehneet_pelaajat[2]), str(Player("Kurri",   "EDM", 37, 53)))

    def test_neljan_eniten_syottoja_antaneen_pelaajan_haku(self):
        eniten_syottoja_antaneet_pelaajat = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(eniten_syottoja_antaneet_pelaajat), 4)

        self.assertEqual(str(eniten_syottoja_antaneet_pelaajat[0]), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertEqual(str(eniten_syottoja_antaneet_pelaajat[1]), str(Player("Yzerman", "DET", 42, 56)))
        self.assertEqual(str(eniten_syottoja_antaneet_pelaajat[2]), str(Player("Lemieux", "PIT", 45, 54)))
        self.assertEqual(str(eniten_syottoja_antaneet_pelaajat[3]), str(Player("Kurri",   "EDM", 37, 53)))

    def test_virheellinen_sortby_parametri_palauttaa_eniten_pisteita_tehneet(self):
        pelaajat = self.stats.top(1, 5)
        self.assertEqual(len(pelaajat), 2)

        self.assertEqual(str(pelaajat[0]), str(Player("Gretzky", "EDM", 35, 89)))
        self.assertEqual(str(pelaajat[1]), str(Player("Lemieux", "PIT", 45, 54)))