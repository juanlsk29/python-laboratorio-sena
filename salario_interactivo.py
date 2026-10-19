nombre = input("Nombre del trabajador: ")
horas = int(input("Horas trabajadas: "))
valor_hora = float(input("Valor por hora: "))

pago_total = horas * valor_hora

print("=========================")
print("     RESUMEN DEL PAGO")
print("=========================")
print("Trabajador:", nombre)
print("Horas:", horas)
print("Valor por hora: $", valor_hora)
print("Pago total: $", pago_total)

#Nombre del trabajador: Juan
#Horas trabajadas: 67
#Valor por hora: 10000
#=========================
#     RESUMEN DEL PAGO
#=========================
#Traabajador: Juan
#Horas: 67
#Valor por hora: $ 10000.0
#Pago total: $ 670000.0