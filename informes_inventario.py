
productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

sin_existencias = [
    producto["nombre"]
    for producto in productos
    if producto["cantidad"] == 0
]

precios_altos = [
    producto["nombre"]
    for producto in productos
    if producto["precio"] > 100000
]

cantidades_diferentes = {
    producto["cantidad"]
    for producto in productos
}

precios_por_nombre = {
    producto["nombre"]: producto["precio"]
    for producto in productos
}

print("Productos sin existencias:", sin_existencias)
print("Productos con precio superior a $100.000:", precios_altos)
print("Cantidades diferentes:", cantidades_diferentes)
print("Nombre y precio:", precios_por_nombre)

#PS C:\Users\PC\Desktop\python-laboratorio2> python informes_inventario.py
#Productos sin existencias: ['Mouse']
#Productos con precio superior a $100.000: ['Monitor']
#Cantidades diferentes: {0, 2, 4}
#Nombre y precio: {'Teclado': 85000, 'Mouse': 45000, 'Monitor': 700000}