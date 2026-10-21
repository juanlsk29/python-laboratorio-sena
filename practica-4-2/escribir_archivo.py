from pathlib import Path

ruta = Path("mensaje.txt")

ruta.write_text(
    "Primer archivo de Python.\n",
    encoding="utf-8"
)

print("Archivo guardado:", ruta)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python escribir_archivo.py
# Archivo guardado: mensaje.txt