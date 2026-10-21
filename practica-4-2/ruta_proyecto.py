from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_DATOS = BASE_DIR / "datos" / "inventario.txt"

RUTA_DATOS.parent.mkdir(parents=True, exist_ok=True)
RUTA_DATOS.write_text("Datos del proyecto\n", encoding="utf-8")

print(RUTA_DATOS)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python ruta_proyecto.py
# C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2\datos\inventario.txt