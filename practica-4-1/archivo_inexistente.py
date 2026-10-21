from pathlib import Path

ruta = Path("archivo_que_no_existe.txt")

try:
    contenido = ruta.read_text(encoding="utf-8")
    print(contenido)
except FileNotFoundError:
    print("No se encontró el archivo solicitado.")

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python archivo_inexistente.py
# No se encontró el archivo solicitado.