notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]

aprobadas = [nota for nota in notas if nota >= 3.0]
reprobadas = [nota for nota in notas if nota < 3.0]
notas_dobladas = [nota * 2 for nota in notas]

print("Notas aprobadas:", aprobadas)
print("Notas inferiores a 3.0:", reprobadas)
print("Notas multiplicadas por 2:", notas_dobladas)

#PS C:\Users\PC\Desktop\python-laboratorio2> python notas_aprobadas.py
#Notas aprobadas: [3.0, 4.8, 3.7, 5.0]
#Notas inferiores a 3.0: [2.5, 1.9]
#Notas multiplicadas por 2: [5.0, 6.0, 9.6, 3.8, 7.4, 10.0]