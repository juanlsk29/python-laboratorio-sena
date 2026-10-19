def calcular_unidades(productos):
    total = 0

    for producto in productos:
        total += producto["cantidad"]

    return total


inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 7}
]

print(calcular_unidades(inventario))
