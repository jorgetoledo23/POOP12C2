#pip install requests
import requests

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

#JavaScript Object Notation
data = r.json()

bpi = data['bpi']
usd = bpi['USD']
eur = bpi['EUR']

valor = usd['rate']
valoreur = eur['rate']

import os
os.system("cls")
print(f"Valor actual del Bitcoin en USD: $${ valor }")
print(f"Valor actual del Bitcoin en EUR: $${ valoreur }")