import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"


def exportar_csv(inventario):
    RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)

    campos = [
        "codigo",
        "nombre",
        "categoria",
        "precio",
        "cantidad",
        "valor_inventario"
    ]

    try:
        with RUTA_CSV.open(
            "w", newline="", encoding="utf-8"
        ) as archivo:
            escritor = csv.DictWriter(
                archivo, fieldnames=campos
            )
            escritor.writeheader()

            for producto in inventario.listar():
                datos = producto.a_diccionario()
                datos["valor_inventario"] = (
                    producto.precio * producto.cantidad
                )
                escritor.writerow(datos)

    except OSError as error:
        raise OSError(f"No se pudo exportar el CSV: {error}") from error

    return RUTA_CSV
