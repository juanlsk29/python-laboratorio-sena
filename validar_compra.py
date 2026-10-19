precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento (%): "))

if precio <= 0 or cantidad <= 0:
    print("El precio y la cantidad deben ser mayores que cero.")
elif descuento < 0 or descuento > 100:
    print("El descuento debe estar entre 0 y 100.")
else:
    subtotal = precio * cantidad
    valor_descuento = subtotal * descuento / 100
    total = subtotal - valor_descuento

    print("Subtotal:", subtotal)
    print("Descuento:", valor_descuento)
    print("Total:", total)

#PS C:\Users\PC\Desktop\python-laboratorio2> python validar_compra.py
#Cantidad: 2
#Descuento (%): 10
#Subtotal: 200000.0
#Descuento: 20000.0
#PS C:\Users\PC\Desktop\python-laboratorio2> python validar_compra.py
#Precio: -50000
#Cantidad: 2
#Descuento (%): 10
#El precio y la cantidad deben ser mayores que cero.
#PS C:\Users\PC\Desktop\python-laboratorio2> python validar_compra.py
#Precio: 50000
#Cantidad: 0
#Descuento (%): 5
#El precio y la cantidad deben ser mayores que cero.
#PS C:\Users\PC\Desktop\python-laboratorio2> python validar_compra.py
#Precio: 80000
#Cantidad: 1
#Descuento (%): 110
#El descuento debe estar entre 0 y 100.

membresia = False
valor_compra = 200000

if membresia and valor_compra >= 150000:
    print("Aplica descuento.")
else:
    print("No aplica descuento.")
