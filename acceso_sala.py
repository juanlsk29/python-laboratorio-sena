edad = int(input("Ingrese su edad: "))
autorizacion = input("¿Tiene autorización? (si/no): ").strip().lower()

if edad >= 18:
    print("Acceso permitido.")
elif edad >= 0 and autorizacion == "si":
    print("Acceso permitido con autorización.")
else:
    print("Acceso no permitido.")

#PS C:\Users\PC\Desktop\python-laboratorio2> python acceso_sala.py
#Ingrese su edad: 20
#¿Tiene autorización? (si/no): no
#Acceso permitido.
#PS C:\Users\PC\Desktop\python-laboratorio2> python acceso_sala.py
#Ingrese su edad: 17
#¿Tiene autorización? (si/no): si
#Acceso permitido con autorización.
#PS C:\Users\PC\Desktop\python-laboratorio2> python acceso_sala.py
#Ingrese su edad: 16
#¿Tiene autorización? (si/no): no
#Acceso no permitido.
#PS C:\Users\PC\Desktop\python-laboratorio2> python acceso_sala.py
#Ingrese su edad: 18
#¿Tiene autorización? (si/no): no
#Acceso permitido.