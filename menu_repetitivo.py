opcion = ""

while opcion != "0":
    print()
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("0. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        print("Hola.")
    elif opcion == "2":
        print("El programa sigue ejecutándose.")
    elif opcion == "0":
        print("Programa terminado.")
    else:
        print("Opción no válida.")

#PS C:\Users\PC\Desktop\python-laboratorio2> python menu_repetitivo.py

#1. Saludar        
#2. Mostrar mensaje
#0. Salir
#Opción: 1
#Hola.

#1. Saludar        
#2. Mostrar mensaje
#0. Salir
#Opción: 2
#El programa sigue ejecutándose.

#1. Saludar
#2. Mostrar mensaje
#0. Salir
#Opción: 0
#Programa terminado.

#¿Qué variable controla el ciclo? 
# numero.



#¿Esa variable cambia? 
# No, siempre vale 1.



#¿La condición dejará de cumplirse? 
# No, porque 1 <= 5 siempre será verdadero mientras la variable no cambie.