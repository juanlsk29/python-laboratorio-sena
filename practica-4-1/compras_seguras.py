cantidad_compras = 0
total_compras = 0.0

while True:
    try:
        importe = float(input("Importe de compra (0 para terminar): "))
    except ValueError:
        print("Error: debes ingresar un número.")
        continue

    if importe == 0:
        break

    if importe < 0:
        print("Error: el importe debe ser positivo.")
        continue

    cantidad_compras += 1
    total_compras += importe

    print("Compra registrada:", importe)

print("\nResumen de compras")
print("Compras aceptadas:", cantidad_compras)
print("Total acumulado:", total_compras)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python compras_seguras.py
# Importe de compra (0 para terminar): 10000
# Compra registrada: 10000.0
# Importe de compra (0 para terminar): abc
# Error: debes ingresar un número.     
# Importe de compra (0 para terminar): -500
# Error: el importe debe ser positivo. 
# Importe de compra (0 para terminar): 20000
# Compra registrada: 20000.0
# Importe de compra (0 para terminar): 0

# Resumen de compras
# Compras aceptadas: 2
# Total acumulado: 30000.0