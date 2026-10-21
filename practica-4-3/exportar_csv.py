import csv
from pathlib import Path

productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0}
]

ruta = Path(__file__).resolve().parent / "reporte.csv"

with ruta.open("w", newline="", encoding="utf-8") as archivo:
    campos = ["codigo", "nombre", "precio", "cantidad"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(productos)

print("Reporte exportado:", ruta)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python exportar_csv.py
# Reporte exportado: C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3\reporte.csv

# RESULTADO 
# codigo,nombre,precio,cantidad
# P001,Teclado,85000,4
# P002,Mouse,45000,0
