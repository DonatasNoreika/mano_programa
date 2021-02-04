
from modules.kursas import Kursas
import requests

kursas = Kursas("Python kursas")
kursas2= Kursas("Java kursas")
print(kursas.pavadinimas)

source = requests.get('https://www.delfi.lt/')
print(source.status_code)
