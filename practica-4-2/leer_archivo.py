from pathlib import Path

ruta = Path("mensaje.txt")

try:
    contenido = ruta.read_text(encoding="utf-8")
    print("Contenido:")
    print(contenido)
except FileNotFoundError:
    print("No se encontró el archivo mensaje.txt.")

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python leer_archivo.py    
# Contenido:
# Primer archivo de Python.