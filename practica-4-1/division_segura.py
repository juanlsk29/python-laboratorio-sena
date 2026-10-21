try:
    numero1 = float(input("Primer número: "))
    numero2 = float(input("Segundo número: "))

except ValueError:
    print("Error: debes ingresar números válidos.")

else:
    if numero2 == 0:
        print("Error: no se puede dividir entre cero.")
    else:
        resultado = numero1 / numero2
        print("Resultado de la división:", resultado)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python division_segura.py
# Primer número: 10
# Segundo número: 2
# Resultado de la división: 5.0
# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python division_segura.py
# Primer número: 10
# Segundo número: 0
# Error: no se puede dividir entre cero.
# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python division_segura.py
# Primer número: abc
# Error: debes ingresar números válidos.