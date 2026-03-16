import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataa_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_ota_saldoa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_ota_saldoa_liikaa(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_sallittu_otto_palauttaa_true(self):
        otto = self.maksukortti.ota_rahaa(500)

        self.assertEqual(otto, True)

    def test_vaara_otto_palauttaa_false(self):
        otto = self.maksukortti.ota_rahaa(2000)

        self.assertEqual(otto, False)

    def test_merkkijono_muoto(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")