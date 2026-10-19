edad = int(input("Ingrese su edad: "))
inscripcion = input("¿Está inscrito? (si/no): ").strip().lower()
documentos = int(input("Número de documentos entregados: "))

cumple_requisitos = True

if edad < 16:
    print("Requisito pendiente: debe tener al menos 16 años.")
    cumple_requisitos = False

if inscripcion != "si":
    print("Requisito pendiente: debe estar inscrito.")
    cumple_requisitos = False

if documentos < 3:
    print("Requisito pendiente: debe entregar al menos 3 documentos.")
    cumple_requisitos = False

if cumple_requisitos:
    print("La solicitud cumple todos los requisitos.")
else:
    print("La solicitud no cumple todos los requisitos.")

#Ingrese su edad: 18
#¿Está inscrito? (si/no): si
#Número de documentos entregados: 3
#La solicitud cumple todos los requisitos.
#PS C:\Users\PC\Desktop\python-laboratorio2> python evaluar_solicitud.py
#Ingrese su edad: 15
#Número de documentos entregados: 3
#Requisito pendiente: debe tener al menos 16 años.
#La solicitud no cumple todos los requisitos.
#PS C:\Users\PC\Desktop\python-laboratorio2> python evaluar_solicitud.py
#Ingrese su edad: 20
#¿Está inscrito? (si/no): no
#Número de documentos entregados: 2
#Requisito pendiente: debe estar inscrito.
#Requisito pendiente: debe entregar al menos 3 documentos.
#La solicitud no cumple todos los requisitos.
#PS C:\Users\PC\Desktop\python-laboratorio2> python evaluar_solicitud.py
#Ingrese su edad: 16
#¿Está inscrito? (si/no): si
#Número de documentos entregados: 2
#Requisito pendiente: debe entregar al menos 3 documentos.
#La solicitud no cumple todos los requisitos.