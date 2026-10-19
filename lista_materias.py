materias = ["Python", "Bases de datos", "HTML", "CSS", "JavaScript"]

print("Lista de materias:")

for posicion, materia in enumerate(materias, start=1):
    print(posicion, "-", materia)

print()

nueva_materia = input("Ingrese una nueva materia: ").strip()
materias.append(nueva_materia)

print()
print("Lista actualizada:")

for posicion, materia in enumerate(materias, start=1):
    print(posicion, "-", materia)

#PS C:\Users\PC\Desktop\python-laboratorio2> python lista_materias.py
#Lista de materias:
#1 - Python
#2 - Bases de datos
#3 - HTML
#4 - CSS
#5 - JavaScript