from moja_biblioteka.importy.importy_ludnosc.importy import *
from moja_biblioteka.importy.importy_pit.pit import *
from moja_biblioteka.porownania.porownania_podlegle.podlegle import  *
from moja_biblioteka.porownania.porownania_rok.porownania_rok import *
from moja_biblioteka.porownania.porownania_pit_mieszkancy.porownaj_pit_mieszkancy import *

def main():

    #porownanie dwóch lat:
    powiaty_2019 = przetworz_powiat(wczytaj_powiat("20200214_Powiaty_za_2019.xlsx"))
    powiaty_2020 = przetworz_powiat(wczytaj_powiat("20210211_Powiaty_za_2020.xlsx"))
    print(porownaj_lata(powiaty_2019, powiaty_2020))

    #policzenie dodchodow na mieszkanca
    gminy_2020 = przetworz_gminy(wczytaj_gminy("20210215_Gminy_2_za_2020 (1).xlsx"))
    ludnosc_gmin = wczytaj_zestawienie_gminy("Tabela_IV.xls")
    print(porownaj_pit_mieszkancy_gmina(gminy_2020, ludnosc_gmin))

    #liczenie wariancji i sreniej dla jednostek podleglych:
    wojewodztwo_2019 = wczytaj_wojewodztwo("20210211_Województwa_za_2020.xlsx")
    print(podlegle_wojewodztwo(powiaty_2019, wojewodztwo_2019))

main()