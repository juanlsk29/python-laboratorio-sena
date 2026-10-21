try:
    cantidad = int("abc")
except ValueError:
    print("El contenido no representa un entero.")

try:
    cantidad = int(None)
except TypeError:
    print("El tipo recibido no permite esa conversión.")

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python conversiones_excepciones.py
# El contenido no representa un entero.
# El tipo recibido no permite esa conversión.