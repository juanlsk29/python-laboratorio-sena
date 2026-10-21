import json
from pathlib import Path

from inventario import Inventario


BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


class ErrorCargaInventario(Exception):
    """Indica que el archivo existente no se pudo recuperar."""


def guardar_inventario(inventario):
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)
    datos = inventario.exportar_datos()

    try:
        with RUTA_JSON.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
    except (OSError, TypeError, ValueError) as error:
        raise OSError(f"No se pudo guardar el inventario: {error}") from error

    return RUTA_JSON


def cargar_inventario():
    inventario = Inventario()

    if not RUTA_JSON.exists():
        return inventario

    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            raise ValueError("El JSON debe contener una lista de productos.")


        inventario.cargar_datos(datos)

    except (OSError, json.JSONDecodeError, ValueError, TypeError) as error:
        raise ErrorCargaInventario(
            f"No se pudo recuperar {RUTA_JSON.name}: {error}"
        ) from error

    return inventario
