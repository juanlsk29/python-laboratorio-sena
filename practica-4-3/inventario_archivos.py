import csv
import json
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
RUTA_JSON = CARPETA / "inventario.json"
RUTA_CSV = CARPETA / "inventario.csv"

productos = []
archivo_danado = False


if RUTA_JSON.exists():
    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            raise ValueError("El JSON debe contener una lista.")

        if not all(isinstance(p, dict) for p in datos):
            raise ValueError("Cada producto debe ser un diccionario.")

        productos = datos
        print("Inventario recuperado:", len(productos), "productos.")

    except (json.JSONDecodeError, ValueError) as error:
        archivo_danado = True
        print("ERROR: el archivo JSON está dañado o tiene datos inválidos.")
        print("Detalle:", error)
        print("No se sobrescribirá el archivo.")
else:
    print("No existe inventario.json. Se iniciará uno vacío.")


while True:
    print("\n--- INVENTARIO ---")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Guardar en JSON")
    print("4. Exportar a CSV")
    print("5. Salir")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        if not productos:
            print("El inventario está vacío.")
        else:
            for producto in productos:
                print(producto)

    elif opcion == "2":
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()

        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            if not codigo or not nombre:
                print("El código y el nombre son obligatorios.")
            elif precio < 0 or cantidad < 0:
                print("El precio y la cantidad no pueden ser negativos.")
            elif any(p.get("codigo") == codigo for p in productos):
                print("Ya existe un producto con ese código.")
            else:
                productos.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })
                print("Producto agregado. Recuerda guardar los cambios.")

        except ValueError:
            print("Precio o cantidad inválidos.")

    elif opcion == "3":
        if archivo_danado:
            print("Guardado bloqueado: revisa y corrige inventario.json primero.")
        else:
            with RUTA_JSON.open("w", encoding="utf-8") as archivo:
                json.dump(productos, archivo, ensure_ascii=False, indent=4)

            print("Inventario guardado en inventario.json.")

    elif opcion == "4":
        campos = ["codigo", "nombre", "precio", "cantidad"]

        with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(productos)

        print("Inventario exportado a inventario.csv.")

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")

# RESULTADO DE TERMINAL


# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python inventario_archivos.py 
# No existe inventario.json. Se iniciará uno vacío.

# --- INVENTARIO ---
# 1. Mostrar productos
# 2. Agregar producto
# 3. Guardar en JSON
# 4. Exportar a CSV
# 5. Salir
# Selecciona una opción: 2
# Código: C001
# Nombre: Computador
# Precio: 10000
# Cantidad: 10
# Producto agregado. Recuerda guardar los cambios.

# --- INVENTARIO ---
# 1. Mostrar productos
# 2. Agregar producto
# 3. Guardar en JSON
# 4. Exportar a CSV
# 5. Salir
# Selecciona una opción: 2
# Código: C002
# Nombre: Mouse
# Precio: 5000
# Cantidad: 2
# Producto agregado. Recuerda guardar los cambios.

# --- INVENTARIO ---
# 1. Mostrar productos
# 2. Agregar producto
# 3. Guardar en JSON
# 4. Exportar a CSV
# 5. Salir
# Selecciona una opción: 2
# Código: C003
# Nombre: Agua
# Precio: 60000
# Cantidad: 20
# Producto agregado. Recuerda guardar los cambios.

# --- INVENTARIO ---
# 1. Mostrar productos
# 2. Agregar producto
# 3. Guardar en JSON
# 4. Exportar a CSV
# 5. Salir
# Selecciona una opción: 1
# {'codigo': 'C001', 'nombre': 'Computador', 'precio': 10000.0, 'cantidad': 10}
# {'codigo': 'C002', 'nombre': 'Mouse', 'precio': 5000.0, 'cantidad': 2}
# {'codigo': 'C003', 'nombre': 'Agua', 'precio': 60000.0, 'cantidad': 20}

# --- INVENTARIO ---
# 1. Mostrar productos
# 2. Agregar producto
# 3. Guardar en JSON
# 4. Exportar a CSV
# 5. Salir
# Selecciona una opción: 3
# Inventario guardado en inventario.json.

# --- INVENTARIO ---
# 1. Mostrar productos
# 2. Agregar producto
# 3. Guardar en JSON
# 4. Exportar a CSV
# 5. Salir
# Selecciona una opción: 4
# Inventario exportado a inventario.csv.

# --- INVENTARIO ---
# 1. Mostrar productos
# 2. Agregar producto
# 3. Guardar en JSON
# 4. Exportar a CSV
# 5. Salir
# Selecciona una opción: 5
# Programa finalizado.

# RESULTADO DE JSON


# [
#     {
#         "codigo": "C001",
#         "nombre": "Computador",
#         "precio": 10000.0,
#         "cantidad": 10
#     },
#     {
#         "codigo": "C002",
#         "nombre": "Mouse",
#         "precio": 5000.0,
#         "cantidad": 2
#     },
#     {
#         "codigo": "C003",
#         "nombre": "Agua",
#         "precio": 60000.0,
#         "cantidad": 20
#     }
# ]


# RESULTADO CSV


# codigo,nombre,precio,cantidad
# C001,Computador,10000.0,10
# C002,Mouse,5000.0,2
# C003,Agua,60000.0,20
