def agotados(productos):
    nombres_agotados = []

    for producto in productos:
        if producto["cantidad"] == 0:
            nombres_agotados.append(producto["nombre"])

    return nombres_agotados


inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 0},
    {"nombre": "Monitor", "cantidad": 0}
]

print("Productos agotados:", agotados(inventario))


def agotados(productos):
    return [
        producto["nombre"]
        for producto in productos
        if producto["cantidad"] == 0
    ]
