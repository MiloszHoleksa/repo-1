import pandas as pd
import numpy as np
procent_pracujacych = 0.8

def porownaj_pit_mieszkancy_gmina(dataframe_pit, dataframe_mieszkancy):
    pit = dataframe_pit
    mieszkancy = dataframe_mieszkancy
    pit = pit.sort_values("ID")
    mieszkancy = mieszkancy.sort_values("ID")
    pit = pit[np.in1d(np.array(pit["ID"]), np.array(mieszkancy["ID"]))]
    mieszkancy = mieszkancy[np.in1d(np.array(mieszkancy["ID"]), np.array(pit["ID"]))]
    pit = pit.reset_index(drop = True)
    mieszkancy = mieszkancy.reset_index(drop = True)
    if not np.array_equal(pit["ID"], mieszkancy["ID"]):
        print("wrong data")
        return NotImplementedError
    podzielone = pit["należności"]/ mieszkancy["ludność"]
    podzielone = (x * procent_pracujacych for x in podzielone)
    porownane = pd.DataFrame({'ID': pit["ID"], 'należności/mieszkańcy': podzielone})
    return porownane

def porownaj_pit_mieszkancy_powiat(dataframe_pit, dataframe_mieszkancy):
    pit = dataframe_pit
    mieszkancy = dataframe_mieszkancy
    pit = pit.sort_values("ID")
    mieszkancy = mieszkancy.sort_values("ID")
    #chwilowy if, zamienić na test
    if not np.array_equal(pit["ID"], mieszkancy["ID"]):
        print("wrong data")
        return NotImplementedError
    podzielone = pit["należności"]/ mieszkancy["ludność"]
    podzielone = (x * procent_pracujacych for x in podzielone)
    porownane = pd.DataFrame({'ID': pit["ID"], 'należności/mieszkańcy': podzielone})
    return porownane

def porownaj_pit_mieszkancy_miasta(dataframe_pit, dataframe_mieszkancy):
    pit = dataframe_pit
    mieszkancy = dataframe_mieszkancy
    pit = pit.sort_values("ID")
    pit = pit[~pit["Nazwa JST"].duplicated(keep='first')]
    pit = pit.reset_index()
    mieszkancy = mieszkancy.sort_values("ID")
    #chwilowy if, zamienić na test
    if not np.array_equal(pit["ID"], mieszkancy["ID"]):
        print("wrong data")
        return NotImplementedError
    podzielone = pit["należności"]/ mieszkancy["ludność"]
    podzielone = (x * procent_pracujacych for x in podzielone)
    porownane = pd.DataFrame({'ID': pit["ID"], 'należności/mieszkańcy': podzielone})
    return porownane

def porownaj_pit_mieszkancy_wojewodztwo(dataframe_pit, dataframe_mieszkancy):
    pit = dataframe_pit
    mieszkancy = dataframe_mieszkancy
    pit = pit.sort_values("Nazwa JST")
    mieszkancy["wojewodztwo"] = mieszkancy["wojewodztwo"].str.lower()
    mieszkancy = mieszkancy.sort_values("wojewodztwo")
    #chwilowy if, zamienić na test
    if not np.array_equal(pit["Nazwa JST"], mieszkancy["wojewodztwo"]):
        print("wrong data")
        return NotImplementedError
    podzielone = pit["należności"]/ mieszkancy["ludność"]
    podzielone = (x * procent_pracujacych for x in podzielone)
    porownane = pd.DataFrame({'wojewodztwo': pit["Nazwa JST"], 'należności/mieszkańcy': podzielone})
    return porownane
