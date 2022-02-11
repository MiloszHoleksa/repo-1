from importy.importy_ludnosc.importy import *
from importy.importy_pit.pit import *
from porownania.porownania_podlegle.podlegle import  *
from porownania.porownania_rok.porownania_rok import *
from porownania.porownania_pit_mieszkancy.porownaj_pit_mieszkancy import *
import unittest

class TestBiblioteki(unittest.TestCase):
    def test_import(self):
        testowy_df = przetworz_zestawienie_wojewodztwo(wczytaj_zestawienie_wojewodztwo(r"testy\dane\ludnosc_testowy.xls"))
        self.assertEqual(testowy_df["wojewodztwo"][0], "Dolnośląskie")

    def test_podlegle(self):
        testowe_woj = wczytaj_wojewodztwo(r"testy\dane\testowe_woj.xlsx")
        testowe_powiaty = przetworz_powiat(wczytaj_powiat(r"testy\dane\testowe_powiaty.xlsx"))
        self.assertEqual(len(podlegle_wojewodztwo(testowe_powiaty, testowe_woj)), 2)

    def  test_rok(self):
        testowe_powiaty2019 = przetworz_powiat(wczytaj_powiat(r"testy\dane\testowe_powiaty.xlsx"))
        testowe_powiaty2020 = przetworz_powiat(wczytaj_powiat(r"testy\dane\testowe_powiaty.xlsx"))
        df = porownaj_lata(testowe_powiaty2019, testowe_powiaty2020)
        self.assertTrue((df['roznica w dochodach'] == 0).all())


if __name__ == '__main__':
    unittest.main()
