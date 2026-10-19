def mostrar_productos(productos):
    for producto in productos:
        print(producto)


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def valor_inventario(productos):
    total = 0

    for producto in productos:
        total += producto["precio"] * producto["cantidad"]

    return total


def productos_sin_stock(productos):
    nombres = []

    for producto in productos:
        if producto["cantidad"] == 0:
            nombres.append(producto["nombre"])

    return nombres


inventario = [
    {"codigo": 101, "nombre": "Teclado", "precio": 80000, "cantidad": 4},
    {"codigo": 102, "nombre": "Mouse", "precio": 40000, "cantidad": 0},
    {"codigo": 103, "nombre": "Monitor", "precio": 600000, "cantidad": 2}
]

print("=== PRODUCTOS ===")
mostrar_productos(inventario)

print("\n=== BÚSQUEDA ===")
print(buscar_producto(inventario, 102))

print("\n=== VALOR DEL INVENTARIO ===")
print(valor_inventario(inventario))

print("\n=== PRODUCTOS SIN STOCK ===")
print(productos_sin_stock(inventario))

# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-1> python inventario_funciones.py 
# === PRODUCTOS ===
# {'codigo': 101, 'nombre': 'Teclado', 'precio': 80000, 'cantidad': 4}
# {'codigo': 102, 'nombre': 'Mouse', 'precio': 40000, 'cantidad': 0}
# {'codigo': 103, 'nombre': 'Monitor', 'precio': 600000, 'cantidad': 2}

# === BÚSQUEDA ===
# {'codigo': 102, 'nombre': 'Mouse', 'precio': 40000, 'cantidad': 0}

# === VALOR DEL INVENTARIO ===
# 1520000

# === PRODUCTOS SIN STOCK ===
# ['Mouse']