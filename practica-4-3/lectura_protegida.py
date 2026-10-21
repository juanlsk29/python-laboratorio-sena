import json
from pathlib import Path

ruta = Path(__file__).resolve().parent / "productos.json"

if not ruta.exists():
    productos = []
    print("El archivo no existe. Se iniciará un inventario vacío.")

else:
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            productos = json.load(archivo)

        if not isinstance(productos, list):
            raise ValueError("El contenido JSON debe ser una lista.")

        print("Productos recuperados:", len(productos))
        print(productos)

    except (json.JSONDecodeError, ValueError) as error:
        print("El archivo existe, pero contiene datos inválidos.")
        print("Detalle:", error)
        print("No se modificó el archivo.")
        print("Revisa su contenido antes de intentar corregirlo.")

# ESCENARIO 1
# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python lectura_protegida.py
# El archivo no existe. Se iniciará un inventario vacío.
# ESCENARIO 2 
# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python lectura_protegida.py
# Productos recuperados: 2
# [{'codigo': 'P001', 'nombre': 'Teclado', 'precio': 85000, 'cantidad': 4}, {'codigo': 'P002', 'nombre': 'Mouse', 'precio': 45000, 'cantidad': 0}]
# ESCENARIO 3
# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python lectura_protegida.py
# El archivo existe, pero contiene datos inválidos.
# Detalle: Expecting ',' delimiter: line 9 column 17 (char 138)
# No se modificó el archivo.
# Revisa su contenido antes de intentar corregirlo.