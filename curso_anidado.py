curso = {
    "nombre": "Fundamentos de Python",
    "codigo": "PY101",
    "temas": [
        "Variables y tipos de datos",
        "Condicionales y ciclos",
        "Listas y diccionarios"
    ],
    "instructor": {
        "nombre": "Esteban",
        "area": "Desarrollo de software"
    }
}

print("Nombre del curso:", curso["nombre"])
print("Segundo tema:", curso["temas"][1])
print("Instructor:", curso["instructor"]["nombre"])
print("Cantidad de temas:", len(curso["temas"]))

#PS C:\Users\PC\Desktop\python-laboratorio2> python curso_anidado.py
#Nombre del curso: Fundamentos de Python
#Segundo tema: Condicionales y ciclos
#Instructor: Esteban
#Cantidad de temas: 3