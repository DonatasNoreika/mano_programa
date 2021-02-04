
from modules.python_kursas import Kursas, PythonKursas
import requests

kursas = Kursas("Python kursas")
kursas2 = Kursas("Java kursas")
kursas3 = PythonKursas("Java kursas")
print(kursas.pavadinimas)

source = requests.get('https://www.delfi.lt/')
print(source.status_code)
