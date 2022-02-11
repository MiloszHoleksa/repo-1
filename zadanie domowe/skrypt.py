from moja_biblioteka.importy.importy_ludnosc.importy import *
from moja_biblioteka.importy.importy_pit.pit import *
from moja_biblioteka.porownania.porownania_podlegle.podlegle import  *
from moja_biblioteka.porownania.porownania_rok.porownania_rok import *
from moja_biblioteka.porownania.porownania_pit_mieszkancy.porownaj_pit_mieszkancy import *

sciezki = {"Powiaty2019": r"dane\20200214_Powiaty_za_2019.xlsx", "Powiaty2020":  r"dane\20210211_Powiaty_za_2020.xlsx",
           "Gminy2020": r"dane\20210215_Gminy_2_za_2020 (1).xlsx", "Gminy2019": r"dane\20200214_Gminy_za_2019.xlsx",
           "Miasta_NPP2019": r"dane\20200214_Miasta_NPP_za_2019.xlsx", "Miasta_NPP2020": r"dane\20210215_Miasta_NPP_2_za_2020 (1).xlsx",
           "Wojewodztwa2019": r"dane\20200214_Wojewodztwa_za_2019.xlsx", "Wojewodztwa2020": r"dane\20210211_Województwa_za_2020.xlsx",
           "Ludnosc_Woj": r"dane\Tabela_II.xls", "Ludnosc_Pow": r"dane\Tabela_III.xls", "Ludnosc_Gmin": r"dane\Tabela_IV.xls"}

print(sciezki)

def main():

    #Porownania roczne
    print("Porownanie roczne: ")
    gminy_2019 = przetworz_powiat(wczytaj_powiat(sciezki["Gminy2019"]))
    gminy_2020 = przetworz_powiat(wczytaj_powiat(sciezki["Gminy2020"]))
    powiaty_2019 = przetworz_powiat(wczytaj_powiat(sciezki["Powiaty2019"]))
    powiaty_2020 = przetworz_powiat(wczytaj_powiat(sciezki["Powiaty2020"]))
    miasta_2019 = przetworz_miasto_pp(wczytaj_miasto_pp(sciezki["Miasta_NPP2019"]))
    miasta_2020 = przetworz_miasto_pp(wczytaj_miasto_pp(sciezki["Miasta_NPP2020"]))
    print("Powiaty: ", porownaj_lata(powiaty_2019, powiaty_2020))
    print("Gminy: ", porownaj_lata(gminy_2019, gminy_2020))
    print("Miasta NPP: ", porownaj_lata(miasta_2019, miasta_2020))


    #policzenie dodchodow na mieszkanca
    ludnosc_gmin = wczytaj_zestawienie_gminy(sciezki["Ludnosc_Gmin"])
    print("Srednie dochody - gminy: ", porownaj_pit_mieszkancy_gmina(gminy_2020, ludnosc_gmin))

    #liczenie wariancji i sreniej dla jednostek podleglych:
    wojewodztwo_2019 = wczytaj_wojewodztwo(sciezki["Wojewodztwa2019"])
    print("Wojewodztwo i podlegle powiaty: ", podlegle_wojewodztwo(powiaty_2019, wojewodztwo_2019))

main()