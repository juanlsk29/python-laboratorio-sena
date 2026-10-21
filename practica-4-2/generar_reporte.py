from pathlib import Path

carpeta = Path("reportes")
carpeta.mkdir(parents=True, exist_ok=True)

ruta = carpeta / "resumen.txt"

contenido = (
    "Reporte de inventario\n"
    "Productos registrados: 15\n"
    "Estado: actualizado\n"
)

ruta.write_text(contenido, encoding="utf-8")

texto = ruta.read_text(encoding="utf-8")

print("Contenido del reporte:")
print(texto)
print("Ruta guardada:", ruta.resolve())

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python generar_reporte.py
# Contenido del reporte:
# Reporte de inventario
# Productos registrados: 15
# Estado: actualizado

# Ruta guardada: C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2\reportes\resumen.txt

# RESULTADO EN resumen.txt
# Reporte de inventario
# Productos registrados: 15
# Estado: actualizado
