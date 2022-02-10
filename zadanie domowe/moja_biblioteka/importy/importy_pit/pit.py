import pandas as pd
import numpy as np


def wczytaj_gminy(filepath):
    gminy = pd.read_excel(filepath
                           , names=["WK", "PK", "GK", "GT", "Nazwa JST", "województwo", "wojewodztwo", "należności", "dochody wykonane"]
                             , skiprows = lambda x: x in range (0,6)
                             , usecols= "A:D,E:G,K:L"
                            , dtype= {"WK": str, "PK": str, "GK": str, "GT": str}
                                )
    return gminy

def przetworz_gminy(gminy):
    gminy.insert(loc = 0 , column = "ID", value = gminy["WK"] + gminy["PK"] + gminy["GK"] + gminy["GT"])
    powiat = gminy.drop(labels = ["WK", "PK", "GK", "GT"], axis = 1)
    return powiat


def wczytaj_powiat(filepath):
    powiat = pd.read_excel(filepath
                           , names=["WK", "PK", "GK", "GT", "Nazwa JST", "województwo", "należności", "dochody wykonane"]
                             , skiprows = lambda x: x in range (0,6)
                             , usecols= "A:F,K:L"
                            , dtype= {"WK": str, "PK": str}
                                )
    return powiat

def przetworz_powiat(powiat):
    powiat.insert(loc = 0 , column = "ID", value = powiat["WK"] + powiat["PK"])
    powiat = powiat.drop(labels = ["WK", "PK"], axis = 1)
    return powiat

def wczytaj_miasto_pp(filepath):
    miasto_pp = pd.read_excel(filepath
                           , names=["WK", "PK", "Nazwa JST", "województwo", "należności", "dochody wykonane"]
                             , skiprows = lambda x: x in range (0,6)
                             , usecols= "A,B,E:F,K:L"
                            , dtype= {"WK": str, "PK": str}
                                )
    return miasto_pp

def przetworz_miasto_pp(miasto):
    miasto.insert(loc = 0 , column = "ID", value = miasto["WK"] + miasto["PK"])
    miasto = miasto.drop(labels = ["WK", "PK"], axis = 1)
    return miasto


'''
def wczytaj_wojewodztwo(filepath):
    woj = pd.read_excel(filepath
                           , names=["WK", "PK", "GK", "GT", "Nazwa JST", "województwo", "należności", "dochody wykonane"]
                             , skiprows = lambda x: x in range (0,6)
                             , usecols= "E,K"
                            , dtype= {"WK": str, "PK": str}
                                )
    return woj
'''


def wczytaj_wojewodztwo(filepath):
    woj = pd.read_excel(filepath
                           , names=["Nazwa JST", "należności"]
                             , skiprows = lambda x: x in range (0,6)
                             , usecols= "E,K"
                                )
    return woj
