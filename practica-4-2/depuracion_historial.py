from pathlib import Path

ruta = Path("historial.txt")

with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write("Registro 1\n")
    archivo.write("Registro 2\n")

print(ruta.read_text(encoding="utf-8"))

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python depuracion_historial.py
# Registro 1
# Registro 2