invitados = []

for numero in range(1, 6):
    nombre = input(f"Ingrese el nombre del invitado {numero}: ").strip()
    invitados.append(nombre)

print()
print("Cantidad de invitados:", len(invitados))
print("Lista de invitados:", invitados)

#PS C:\Users\PC\Desktop\python-laboratorio2> python invitados.py
#Ingrese el nombre del invitado 1: Juan
#Ingrese el nombre del invitado 2: Anthony
#Ingrese el nombre del invitado 3: Vocero
#Ingrese el nombre del invitado 4: Kevin
#Ingrese el nombre del invitado 5: Yohan  

#Cantidad de invitados: 5
#Lista de invitados: ['Juan', 'Anthony', 'Vocero', 'Kevin', 'Yohan']