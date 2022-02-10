import pandas as pd
import numpy as np


def wczytaj_zestawienie_gminy(filepath):
    zestawienie = pd.read_excel(filepath
                                 , skiprows = lambda x: x in range(0,8)
                                 , usecols= "A:C"
                                , names = ["gmina", "ID", "ludność"]
                                , dtype = {"ID": str}
                                )
    return zestawienie

def przetworz_zestawienie_gminy(zestawienie):
    zestawienie = (zestawienie[~zestawienie["gmina"].str.contains("WOJ.")])
    zestawienie = zestawienie.reset_index(drop = True)
    return zestawienie



def wczytaj_zestawienie_powiat(filepath):
    zestawienie = pd.read_excel(filepath
                                 , skiprows = lambda x: x in range(0,8)
                                 , usecols= "A:C"
                                , names = ["wojewodztwo", "ID", "ludność"]
                                , dtype = {"ID": str}
                                )
    return zestawienie

def przetworz_zestawienie_powiat(zestawienie, miasta = False):
    zestawienie = (zestawienie[~zestawienie["wojewodztwo"].str.contains("Woj.")])
    if miasta == False:
        zestawienie = (zestawienie[~zestawienie["wojewodztwo"].str.contains("M.")])
    else:
        zestawienie = (zestawienie[zestawienie["wojewodztwo"].str.contains("M.")])
    zestawienie = zestawienie.reset_index(drop = True)
    return zestawienie

def wczytaj_zestawienie_wojewodztwo(filepath):
    zestawienie = pd.read_excel(filepath
                                , skiprows = lambda x: (x in range(0,7))
                                , usecols= "A:B"
                                , names = ["wojewodztwo", "ludność"]
                                )
    return zestawienie

def przetworz_zestawienie_wojewodztwo(wojewodztwo):
    wojewodztwo = wojewodztwo[wojewodztwo.index <= 15]
    return wojewodztwo