import pandas as pd

def porownaj_lata(rok1, rok2):
    powiaty_1920 = pd.concat([rok1["należności"],
                              rok2["należności"]],
                             axis = 1,
                             keys = ["2019", "2020"])
    powiaty_1920.insert(loc = 2, column = "roznica w dochodach", value = powiaty_1920["2020"]-powiaty_1920["2019"])
    return powiaty_1920

