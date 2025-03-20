import os
os.system('cls')
print("\n")

import pandas
from datetime import datetime, timedelta
import ctypes
 
a = pandas.read_csv("saraksts.csv", sep=";", dtype=str)

today = datetime.today().strftime("%d.%m")
tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d.%m")

input_date = input("Ievadiet datumu (DD.MM): ")
try:
    datetime.strptime(input_date, "%d.%m")
except ValueError:
    print("Nepareizs datuma formāts. Lūdzu, ievadiet datuma formāta (DD.MM)")
    exit()

 
a["Dzimšanas datums"] = a["Dzimšanas datums"].str[:5]
 
bd_today = a[a["Dzimšanas datums"] == today]
bd_tomorrow = a[a["Dzimšanas datums"] == tomorrow]
 
if not bd_today.empty or not bd_tomorrow.empty:
    teksts = "Šodienas un rītdienas dzimšanas dienas!!!\n\n"
   
    if not bd_today.empty:
        teksts += f"Šodien, {today}:\n"
        for _, row in bd_today.iterrows():
            teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
   
    if not bd_tomorrow.empty:
        teksts += f"Rīt, {tomorrow}:\n"
        for _, row in bd_tomorrow.iterrows():
            teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
else:
    teksts = "Nav neviena dzimšanas diena šodien vai rīt!!!"

ctypes.windll.user32.MessageBoxW(0, teksts.strip(), "svinam", 1)
 