from pathlib import Path

carpeta = Path("datos")
carpeta.mkdir(parents=True, exist_ok=True)

ruta = carpeta / "inventario.txt"
ruta.write_text("Inventario inicial\n", encoding="utf-8")

print("Ubicación:", ruta)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python crear_carpeta.py
# Ubicación: datos\inventario.txt

# RESULTADO DE CARPETA
# Inventario inicial
