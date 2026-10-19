productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000.0, "cantidad": 7},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000.0, "cantidad": 2}
]

print("Registro del cuarto producto")

codigo = input("Código: ").strip()
nombre = input("Nombre: ").strip()
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

nuevo_producto = {
    "codigo": codigo,
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}

productos.append(nuevo_producto)

print("\nCatálogo completo:")

for producto in productos:
    print(
        producto["codigo"], "-",
        producto["nombre"], "- Precio:",
        producto["precio"], "- Cantidad:",
        producto["cantidad"]
    )

#PS C:\Users\PC\Desktop\python-laboratorio2> python catalogo_diccionarios.py
#Registro del cuarto producto
#Código: P001
#Nombre: Agua
#Precio: 1500
#Cantidad: 5

#Catálogo completo:
#P001 - Teclado - Precio: 85000.0 - Cantidad: 4 
#P002 - Mouse - Precio: 45000.0 - Cantidad: 7   
#P003 - Monitor - Precio: 700000.0 - Cantidad: 2
#P001 - Agua - Precio: 1500.0 - Cantidad: 5  

#PS C:\Users\PC\Desktop\python-laboratorio2> python catalogo_diccionarios.py
#Registro del cuarto producto
#Código: P001
#Nombre: Agua     
#Precio: 1500
#Cantidad: 5

#Catálogo completo:
#P001 - Teclado - Precio: 85000.0 - Cantidad: 4 
#P002 - Mouse - Precio: 45000.0 - Cantidad: 7   
#P003 - Monitor - Precio: 700000.0 - Cantidad: 2
#P001 - Agua - Precio: 1500.0 - Cantidad: 5  