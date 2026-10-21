import json
from pathlib import Path

ruta = Path(__file__).resolve().parent / "productos.json"

with ruta.open("r", encoding="utf-8") as archivo:
    productos = json.load(archivo)

for producto in productos:
    print(producto["codigo"], "-", producto["nombre"])

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python leer_json.py
# P001 - Teclado
# P002 - Mouse