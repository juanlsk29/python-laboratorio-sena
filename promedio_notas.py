cantidad = int(input("Cantidad de notas: "))

if cantidad <= 0:
    print("La cantidad de notas debe ser mayor que cero.")
else:
    suma = 0

    for numero in range(1, cantidad + 1):
        nota = float(input("Nota " + str(numero) + ": "))
        suma = suma + nota

    promedio = suma / cantidad

    print("Promedio:", promedio)

#PS C:\Users\PC\Desktop\python-laboratorio2> python promedio_notas.py
#Cantidad de notas: 3
#Nota 1: 4.0
#Nota 2: 3.5
#Nota 3: 4.5
#Promedio: 4.0