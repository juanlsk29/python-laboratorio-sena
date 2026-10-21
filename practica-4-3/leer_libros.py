import json
from pathlib import Path

ruta = Path(__file__).resolve().parent / "libros.json"

with ruta.open("r", encoding="utf-8") as archivo:
    libros = json.load(archivo)

for libro in libros:
    print(f"Código: {libro['codigo']}")
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Año: {libro['anio']}")
    print("-" * 30)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python leer_libros.py
# Código: L001
# Título: Cien años de soledad
# Autor: Gabriel García Márquez
# Año: 1967
# ------------------------------
# Código: L002
# Título: Don Quijote de la Mancha
# Autor: Miguel de Cervantes
# Año: 1605
# ------------------------------
# Código: L003
# Título: El principito
# Autor: Antoine de Saint-Exupéry
# Año: 1943
# ------------------------------