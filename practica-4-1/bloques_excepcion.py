try:
    numero = int(input("Número: "))
except ValueError:
    print("Entrada no numérica.")
else:
    print("Número aceptado:", numero)
finally:
    print("Finalizó el intento de lectura.")

# PS C:\Users\PC\Desktop\python-laboratorio-4> cd practica-4-1                   
# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python bloques_excepcion.py       
# Número: 10
# Número aceptado: 10
# Finalizó el intento de lectura.
# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python bloques_excepcion.py
# Número: hola
# Entrada no numérica.
# Finalizó el intento de lectura.