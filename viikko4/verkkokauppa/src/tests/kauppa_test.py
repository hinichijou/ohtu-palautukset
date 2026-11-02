import unittest
from unittest.mock import Mock, ANY, call
from kauppa import Kauppa
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.side_effect = [42, 43, 44]

        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 20
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "puuro", 2)
            if tuote_id == 3:
                return Tuote(3, "kahvi", 4)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock,
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumeroilla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_maksettaessa_kaksi_eri_ostosta_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumeroilla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 7)

    def test_maksettaessa_kaksi_samaa_ostosta_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumeroilla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_maksettaessa_ostos_jota_on_varastossa_ja_ostos_jota_ei_ole_varastossa_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumeroilla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että ostosten hinnat ovat oikein
        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list,
            [
                call(ANY, ANY, ANY, ANY, 5),
                call(ANY, ANY, ANY, ANY, 2),
            ],
        )

    def test_uusi_viite_jokaiselle_maksutapahtumalle(self):
            self.kauppa.aloita_asiointi()
            self.kauppa.lisaa_koriin(1)
            self.kauppa.tilimaksu("pekka", "12345")

            self.kauppa.aloita_asiointi()
            self.kauppa.lisaa_koriin(1)
            self.kauppa.tilimaksu("hillevi", "22345")

            self.kauppa.aloita_asiointi()
            self.kauppa.lisaa_koriin(2)
            self.kauppa.tilimaksu("uolevi", "12355")

            # varmistetaan, että maksuissa on käytetty eri viitteitä järjestyksessä 42, 43 ja 44
            self.assertEqual(
                self.pankki_mock.tilisiirto.call_args_list,
                [
                    call(ANY, 42, ANY, ANY, ANY),
                    call(ANY, 43, ANY, ANY, ANY),
                    call(ANY, 44, ANY, ANY, ANY),
                ],
            )

    def test_poista_korista_poistaa_tuotteen_maksutapahtumasta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumeroilla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 7)
