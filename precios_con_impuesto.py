precios = [10000, 20000, 50000, 80000]

# Forma 1: ciclo tradicional
precios_for = []

for precio in precios:
    precio_con_impuesto = precio * 1.19
    precios_for.append(precio_con_impuesto)

# Forma 2: comprensión de listas
precios_comprension = [precio * 1.19 for precio in precios]

print("Precios originales:", precios)
print("Con for:", precios_for)
print("Con comprensión:", precios_comprension)

#PS C:\Users\PC\Desktop\python-laboratorio2> python precios_con_impuesto.py
#Precios originales: [10000, 20000, 50000, 80000]
#Con for: [11900.0, 23800.0, 59500.0, 95200.0]        
#Con comprensión: [11900.0, 23800.0, 59500.0, 95200.0]