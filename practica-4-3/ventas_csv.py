import csv
from pathlib import Path

ventas = [
    {"codigo": "V001", "producto": "Teclado", "cantidad": 2, "total": 170000},
    {"codigo": "V002", "producto": "Mouse", "cantidad": 3, "total": 135000},
    {"codigo": "V003", "producto": "Monitor", "cantidad": 1, "total": 450000},
    {"codigo": "V004", "producto": "Audífonos", "cantidad": 2, "total": 100000}
]

ruta = Path(__file__).resolve().parent / "ventas.csv"

with ruta.open("w", newline="", encoding="utf-8") as archivo:
    campos = ["codigo", "producto", "cantidad", "total"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(ventas)

total_vendido = 0

with ruta.open("r", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for venta in lector:
        total_vendido += float(venta["total"])

print("Archivo exportado:", ruta.name)
print("Ventas registradas:", len(ventas))
print("Total vendido:", total_vendido)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python ventas_csv.py
# Archivo exportado: ventas.csv
# Ventas registradas: 4
# Total vendido: 855000.0

# RESULTADO CSV 
# codigo,producto,cantidad,total
# V001,Teclado,2,170000
# V002,Mouse,3,135000
# V003,Monitor,1,450000
# V004,Audífonos,2,100000
