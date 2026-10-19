tareas = []
opcion = ""

while opcion != "0":
    print()
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Consultar cantidad")
    print("0. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        tarea = input("Ingrese la tarea: ").strip()

        if tarea == "":
            print("La tarea no puede estar vacía.")
        else:
            tareas.append(tarea)
            print("Tarea agregada correctamente.")

    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas registradas.")
        else:
            print("Lista de tareas:")

            for posicion, tarea in enumerate(tareas, start=1):
                print(posicion, "-", tarea)

    elif opcion == "3":
        print("Cantidad de tareas:", len(tareas))

    elif opcion == "0":
        print("Programa terminado.")

    else:
        print("Opción no válida.")

#PS C:\Users\PC\Desktop\python-laboratorio2> python lista_tareas.py

#1. Agregar tarea       
#2. Mostrar tareas      
#3. Consultar cantidad  
#0. Salir
#Seleccione una opción: 1
#Ingrese la tarea: Programacion
#Tarea agregada correctamente.

#1. Agregar tarea
#2. Mostrar tareas
#3. Consultar cantidad
#0. Salir
#Seleccione una opción: 2
#Lista de tareas:
#1 - Programacion

#1. Agregar tarea
#2. Mostrar tareas
#3. Consultar cantidad
#0. Salir
#Seleccione una opción: 3
#Cantidad de tareas: 1

#1. Agregar tarea
#2. Mostrar tareas
#3. Consultar cantidad
#0. Salir
#Seleccione una opción: 0
#Programa terminado.