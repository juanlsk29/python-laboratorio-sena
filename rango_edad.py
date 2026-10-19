edad = int(input("Ingrese su edad: "))

if 18 <= edad <= 65:
    print("Edad dentro del rango permitido.")
else:
    print("Edad fuera del rango permitido.")

#PS C:\Users\PC\Desktop\python-laboratorio2> python rango_edad.py
#Ingrese su edad: 17
#Edad fuera del rango permitido.
#PS C:\Users\PC\Desktop\python-laboratorio2> python rango_edad.py
#Ingrese su edad: 18
#Edad dentro del rango permitido.
#PS C:\Users\PC\Desktop\python-laboratorio2> python rango_edad.py
#Ingrese su edad: 65
#Edad dentro del rango permitido.
#PS C:\Users\PC\Desktop\python-laboratorio2> python rango_edad.py
#Ingrese su edad: 66
#Edad fuera del rango permitido.