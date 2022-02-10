import pandas as pd
import numpy as np

def podlegle_wojewodztwo(przetworzony_powiat, przetworzone_wojewodztwo):
    wojewodztwo = przetworzone_wojewodztwo
    powiat = przetworzony_powiat
    powiat_var = powiat.groupby("województwo")["należności"].var()
    wojewodztwo_srednia = pd.DataFrame(powiat.groupby("województwo")["należności"].mean())
    wojewodztwo_srednia = wojewodztwo_srednia.rename(columns={'należności': 'średnia'})
    wojewodztwo_srednia = wojewodztwo_srednia.sort_values("województwo")
    wojewodztwo = wojewodztwo.sort_values("Nazwa JST")
    wojewodztwo = wojewodztwo.set_index("Nazwa JST")
    wojewodztwo_wynik = pd.concat([wojewodztwo, wojewodztwo_srednia], axis = 1)
    return powiat_var, wojewodztwo_wynik


def podlegle_powiat(przetworzone_gminy, przetworzony_powiat):
    powiat = przetworzony_powiat
    gminy = przetworzone_gminy
    gminy_var = gminy.groupby("wojewodztwo")["należności"].var()
    powiat_srednia = pd.DataFrame(gminy.groupby("wojewodztwo")["należności"].mean())
    powiat_srednia = powiat_srednia.rename(columns={'należności': 'średnia'})
    powiat_srednia = powiat_srednia.sort_values("wojewodztwo")
    powiat = powiat.sort_values("Nazwa JST")
    powiat = powiat.set_index("Nazwa JST")
    powiat = powiat.drop(labels = ["GK", "GT", "województwo", "dochody wykonane"], axis = 1)

    powiat = powiat[np.in1d(np.array(powiat.index), np.array(powiat_srednia.index))]
    powiat_srednia = powiat_srednia[np.in1d(np.array(powiat_srednia.index), np.array(powiat.index))]
    powiat = powiat[~powiat.index.duplicated(keep='first')]
    powiat_wynik = pd.concat([powiat, powiat_srednia], axis = 1)
    return gminy_var, powiat_wynik
