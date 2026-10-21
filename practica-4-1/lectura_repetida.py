while True:
    try:
        precio = float(input("Precio: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if precio <= 0:
        print("El precio debe ser positivo.")
        continue

    print("Precio aceptado:", precio)
    break

# PS C:\Users\PC\Desktop\python-laboratorio-4> cd practica-4-1
# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python lectura_repetida.py
# Precio: abc
# Debes escribir un número.
# Precio: -100
# El precio debe ser positivo.
# Precio: 50000
# Precio aceptado: 50000.0