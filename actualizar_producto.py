producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0,
    "cantidad": 4
}

nuevo_precio = float(input("Ingresa el nuevo precio: "))

if nuevo_precio > 0:
    producto["precio"] = nuevo_precio
    print("Precio actualizado correctamente.")
else:
    print("Error: el precio debe ser mayor que cero.")

print("\nDatos del producto:")

for clave, valor in producto.items():
    print(clave, ":", valor)

#PS C:\Users\PC\Desktop\python-laboratorio2> python actualizar_producto.py
#Ingresa el nuevo precio: 50000
#Precio actualizado correctamente.

#Datos del producto:
#codigo : P001
#nombre : Teclado
#precio : 50000.0
#cantidad : 4