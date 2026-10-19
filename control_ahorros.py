total = 0
depositos = 0

while True:
    deposito = int(input("Depósito (0 para terminar): "))

    if deposito == 0:
        break

    if deposito < 0:
        print("El depósito debe ser positivo.")
    else:
        total += deposito
        depositos += 1
        print("Ahorro acumulado:", total)
        print()

print()
print("Depósitos válidos:", depositos)
print("Total ahorrado:", total)

#PS C:\Users\PC\Desktop\python-laboratorio2> python control_ahorros.py
#Depósito (0 para terminar): 10000
#Ahorro acumulado: 10000     

#Depósito (0 para terminar): -5000
#El depósito debe ser positivo.
#Depósito (0 para terminar): 25000
#Ahorro acumulado: 35000     

#Depósito (0 para terminar): 0

#Depósitos válidos: 2
#Total ahorrado: 35000