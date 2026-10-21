import json
from pathlib import Path

libros = [
    {
        "codigo": "L001",
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "anio": 1967
    },
    {
        "codigo": "L002",
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "anio": 1605
    },
    {
        "codigo": "L003",
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "anio": 1943
    }
]

ruta = Path(__file__).resolve().parent / "libros.json"

with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(libros, archivo, ensure_ascii=False, indent=4)

print("Libros guardados correctamente.")

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python libros_json.py
# Libros guardados correctamente.

# RESULTADO DEL JSON 
# [
#     {
#         "codigo": "L001",
#         "titulo": "Cien años de soledad",
#         "autor": "Gabriel García Márquez",
#         "anio": 1967
#     },
#     {
#         "codigo": "L002",
#         "titulo": "Don Quijote de la Mancha",
#         "autor": "Miguel de Cervantes",
#         "anio": 1605
#     },
#     {
#         "codigo": "L003",
#         "titulo": "El principito",
#         "autor": "Antoine de Saint-Exupéry",
#         "anio": 1943
#     }
# ]