

- Problema 1 — UTF-8: Se agregó o verificó encoding="utf-8" en la lectura y escritura de archivos. Se comprobó que los caracteres especiales se conservaran correctamente.

almacenamiento.py
ef guardar_inventario(inventario):
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)
    datos = inventario.exportar_datos()

    try:
        with RUTA_JSON.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
    except (OSError, TypeError, ValueError) as error:
        raise OSError(f"No se pudo guardar el inventario: {error}") from error

    return RUTA_JSON
CODIGO FUNCIONAL
   {
        "codigo": "P009",
        "nombre": "ñoño",
        "categoria": "Accesorios",
        "precio": 50000.0,
        "cantidad": 5
    }

- Problema 2 — Rutas: Se construyeron las rutas desde Path(__file__).resolve().parent para evitar que dependan de la carpeta desde la que se ejecuta Python.

almacenamiento.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"

reportes.py

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"
codigo,nombre,categoria,precio,cantidad,valor_inventario
P001,Teclado,Periféricos,85000.0,4,340000.0
P002,Mouse,Periféricos,45000.0,5,225000.0
P003,Monitor,Componentes,700000.0,2,1400000.0
P005,Agua,Componentes,10000.0,5,50000.0
P006,Espada,Accesorios,5000.0,1,5000.0
P007,Ram8,Componentes,90000.0,0,0.0
P008,Leche,Accesorios,20000.0,2,40000.0
P009,ñoño,Accesorios,50000.0,5,250000.0


- Problema 3 — Serialización: Se creó o verificó el método a_diccionario() y se convirtió cada producto a un diccionario antes de guardarlo con json.dump().

producto.py 

def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

almacenamiento.py

def guardar_inventario(inventario):
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)
    datos = inventario.exportar_datos()

producto.py

def exportar_datos(self):
    return [producto.a_diccionario() for producto in self._productos]ç

    {
        "codigo": "P008",
        "nombre": "Leche",
        "categoria": "Accesorios",
        "precio": 20000.0,
        "cantidad": 2
    },


- Problema 4 — Códigos duplicados: Se validaron los productos en un inventario temporal. Si un registro falla, no se reemplaza el inventario original por una carga parcial.

inventario.py 

 def cargar_datos(self, registros):
        temporal = Inventario()
             for registro in registros:
            producto = Producto.desde_diccionario(registro)
            temporal.registrar(producto)


- Problema 5 — JSON dañado: Se evitó recuperar el inventario como una lista vacía cuando el archivo existente es inválido. El programa informa del error y bloquea el guardado para proteger los datos.

if not RUTA_JSON.exists():
    return inventario

except (OSError, json.JSONDecodeError, ValueError, TypeError) as error:
    raise ErrorCargaInventario(
        f"No se pudo recuperar {RUTA_JSON.name}: {error}"
    ) from error

- Problema 6 — Valor del inventario: Se corrigió el cálculo para multiplicar el precio por la cantidad de cada producto y sumar los resultados.

inventario.py
valor = sum(p.precio * p.cantidad for p in self._productos)

Productos registrados: 3
Unidades totales: 6
Valor total: $1.740.000


- Problema 7 — Persistencia: Se verificó que las modificaciones aceptadas intentan guardarse inmediatamente. Si falla la escritura, el programa informa del error y no anuncia un guardado exitoso.

def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"El valor debe ser como mínimo {minimo}.")
                continue

            return valor
        except ValueError:
            print("Entrada inválida. Escribe un número entero.")


def leer_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje))

            # La validación definitiva también se realiza en Producto.
            import math
            if not math.isfinite(valor) or valor <= 0:
                print("El precio debe ser positivo y finito.")
                continue

            return valor
        except ValueError:
            print("Precio inválido. Escribe un número válido.")


def mostrar_menu():
    print("\n================================")
    print("        GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Guardar inventario")
    print("9. Exportar reporte CSV")
    print("0. Salir")


def guardar_cambios(inventario):
    try:
        ruta = guardar_inventario(inventario)
        print("Inventario guardado correctamente:", ruta)
    except OSError as error:
        print(error)
        print("Los cambios podrían existir solamente en memoria.")