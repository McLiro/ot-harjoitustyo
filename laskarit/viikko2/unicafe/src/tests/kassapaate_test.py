import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_uusi_kassapaate_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_uusi_kassapaate_myytyja_lounaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0.0)
        self.assertEqual(self.kassapaate.edulliset, 0.0)

    def test_maukkaan_lounaan_kateisosto(self):
        self.kassapaate.syo_maukkaasti_kateisella(500.0)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(self.kassapaate.maukkaat, 1.0)

    def test_edullisen_lounaan_kateisosto(self):
        self.kassapaate.syo_edullisesti_kateisella(500.0)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)
        self.assertEqual(self.kassapaate.edulliset, 1.0)

    def test_maukkaan_lounaan_kateinen_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(200.0)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.maukkaat, 0.0)

    def test_edullisen_lounaan_kateinen_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200.0)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0.0)

    def test_maukkaan_lounaan_korttiosto(self):
        kortti = Maksukortti(1000.0)
        osto = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(osto, True)
        self.assertEqual(kortti.saldo_euroina(), 6.0)
        self.assertEqual(self.kassapaate.maukkaat, 1.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_edullisen_lounaan_korttiosto(self):
        kortti = Maksukortti(1000.0)
        osto = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(osto, True)
        self.assertEqual(kortti.saldo_euroina(), 7.6)
        self.assertEqual(self.kassapaate.edulliset, 1.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_maukkaan_lounaan_saldo_ei_riita(self):
        kortti = Maksukortti(200.0)
        osto = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(osto, False)
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.maukkaat, 0.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_edullisen_lounaan_saldo_ei_riita(self):
        kortti = Maksukortti(200.0)
        osto = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(osto, False)
        self.assertEqual(kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.maukkaat, 0.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kortin_lataaminen(self):
        kortti = Maksukortti(1000.0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500.0)

        self.assertEqual(kortti.saldo_euroina(), 15.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.0)

    def test_kortin_lataaminen_negatiivisilla_luvuilla(self):
        kortti = Maksukortti(1000.0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -500.0)

        self.assertEqual(kortti.saldo_euroina(), 10.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)