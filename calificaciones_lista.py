calificaciones = [3.5, 4.2, 2.8, 5.0, 3.5, 4.7]

print("Tres primeras:", calificaciones[:3])
print("Dos últimas:", calificaciones[-2:])
print("Cantidad total:", len(calificaciones))

ordenadas = sorted(calificaciones)
print("Ordenadas de menor a mayor:", ordenadas)
print("Lista original:", calificaciones)

nota_buscada = float(input("¿Qué nota deseas contar?: "))
cantidad = calificaciones.count(nota_buscada)

print("La nota", nota_buscada, "aparece", cantidad, "veces.")

#PS C:\Users\PC\Desktop\python-laboratorio2> python calificaciones_lista.py
#Tres primeras: [3.5, 4.2, 2.8]
#Dos últimas: [3.5, 4.7]
#Cantidad total: 6
#Ordenadas de menor a mayor: [2.8, 3.5, 3.5, 4.2, 4.7, 5.0]
#Lista original: [3.5, 4.2, 2.8, 5.0, 3.5, 4.7]
#¿Qué nota deseas contar?: 4.2
#La nota 4.2 aparece 1 veces.