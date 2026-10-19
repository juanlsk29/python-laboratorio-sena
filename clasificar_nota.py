nota = float(input("Nota: "))

if nota >= 4.5:
    print("Desempeño sobresaliente")
elif nota >= 4.0:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Aprobado")
else:
    print("No aprobado")

#Si cambiamos el orden las ordenes se ejecutan en el orden que vienen por ende si ponemos 4.8 estando el if de 3.0 de primeras todos los valores siguientes seran "aprobado"

respuesta = input("Escribe SI para continuar: ")

#if respuesta == "SI":
#    print("Continuando...")
#else:
#    print("Respuesta diferente de SI.")

#Escribe SI para continuar: SI, si y Si
#Respuesta diferente de SI.
#PS C:\Users\Aprendiz\Desktop\python-laboratorio2> python clasificar_nota.py
#Nota: 5.0
#Desempeño sobresaliente
#Escribe SI para continuar: si
#Respuesta diferente de SI.
#PS C:\Users\Aprendiz\Desktop\python-laboratorio2> python clasificar_nota.py
#Nota: 5.0
#Desempeño sobresaliente
#Escribe SI para continuar: SI
#Continuando...

respuesta = input("Escribe SI para continuar: ").strip().lower()

if respuesta == "si":
    print("Continuando...")
else:
    print("Respuesta diferente de SI.")