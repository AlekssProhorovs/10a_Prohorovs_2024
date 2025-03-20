import os
os.system('cls')
print("\n")

import pandas
from datetime import datetime
import ctypes

a = pandas.read_csv("saraksts.csv", sep=";", dtype=str)
#print(a)
#print(a.to_string())
input_date = input("Ievadiet datumu (DD.MM): ")
try:
    datetime.strptime(input_date, "%d.%m")
except ValueError:
    print("Nepareizs datuma formāts. Lūdzu, ievadiet datuma formāta (DD.MM)")
    exit()

a["Dzimšanas datums"] = a["Dzimšanas datums"].str[:5]

bd_skoleni = a[a["Dzimšanas datums"] == input_date]
print(bd_skoleni)

if not bd_skoleni.empty:
    teksts = "Sveicam dzimšanas dienā!!!\n\n"
    for _, row in bd_skoleni.iterrows():
        teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
else:
    teksts = "šodien un rīt nav nevienam dzimšanas diena!!!"

ctypes.windll.user32.MessageBoxW(0,teksts.strip(), "DZIMŠANAS DIENAS", 1)


