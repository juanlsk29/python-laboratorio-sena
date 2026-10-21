import json
from pathlib import Path

ruta = Path(__file__).resolve().parent / "productos_copia.json"

try:
    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    print("JSON válido.")
    print("Productos:", len(productos))

except json.JSONDecodeError as error:
    print("JSON inválido:", error)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python comprobar_json.py
# JSON válido.
# Productos: 2