import csv
from pathlib import Path

ruta = Path(__file__).resolve().parent / "reporte.csv"

if not ruta.exists():
    print("No existe reporte.csv. Ejecuta primero exportar_csv.py.")
else:
    with ruta.open("r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for producto in lector:
            print(
                producto["codigo"],
                producto["nombre"],
                producto["precio"]
            )

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python leer_csv.py
# P001 Teclado 85000
# P002 Mouse 45000