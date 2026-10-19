
while True:
    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Debes escribir un entero.")
        print()
        continue

    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        print()
        continue

    print("Cantidad aceptada:", cantidad)
    break

# PS C:\Users\PC\Desktop\python-laboratorio3> cd practica-3-4      
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-4> python leer_cantidad.py
# Cantidad: abc
# Debes escribir un entero.

# Cantidad: -2 
# La cantidad no puede ser negativa.

# Cantidad: 5
# Cantidad aceptada: 5