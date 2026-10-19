
try:
    precio = float(input("Precio: "))
    print("Precio ingresado:", precio)
except ValueError:
    print("Debes escribir un número válido.")


# PS C:\Users\PC\Desktop\python-laboratorio3> cd practica-3-4    
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-4> python leer_precio.py
# Precio: 85000
# Precio ingresado: 85000.0
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-4> python leer_precio.py
# Precio: abc
# Debes escribir un número válido.