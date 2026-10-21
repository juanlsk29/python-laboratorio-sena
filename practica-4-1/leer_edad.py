try:
    edad = int(input("Ingresa tu edad: "))
except ValueError:
    print("Error: debes ingresar un número entero.")
else:
    if edad < 0 or edad > 120:
        print("Error: la edad debe estar entre 0 y 120.")
    else:
        print("Edad válida:", edad)
