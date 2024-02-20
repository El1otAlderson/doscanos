
    

import requests
import threading
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


print("Wpisz nazwe strony przyklad:  https://example.com")
x = input()
def sprawdz_katalog(domena, katalog):
    url = x + "/" + katalog
    odpowiedz = requests.get(url, verify=False)
    if odpowiedz.status_code == 200:
        print(f"Katalog {katalog} istnieje na stronie {domena}")
    


plik = open("katalogi.txt", "r")
katalogi = plik.readlines()
plik.close()
katalogi = [k.strip() for k in katalogi]

watkid = []
for katalog in katalogi:
    watkid.append(threading.Thread(target=sprawdz_katalog, args=(x, katalog)))
    watkid[-1].start()

for watek in watkid:
    watek.join()

