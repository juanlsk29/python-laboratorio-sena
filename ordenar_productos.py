productos = ["Teclado", "Mouse", "Monitor", "Cámara", "Parlantes"]

print("Primeros dos:", productos[0:2])
print("Desde el tercero:", productos[2:])
print("Primeros tres:", productos[:3])
print("Últimos dos:", productos[-2:])

ordenados = sorted(productos)

print("Original:", productos)
print("Ordenados:", ordenados)

productos.sort()
print("Lista después de sort():", productos)

#PS C:\Users\PC\Desktop\python-laboratorio2> python ordenar_productos.py
#Primeros dos: ['Teclado', 'Mouse']
#Desde el tercero: ['Monitor', 'Cámara', 'Parlantes']
#Primeros tres: ['Teclado', 'Mouse', 'Monitor']
#Últimos dos: ['Cámara', 'Parlantes']
#Original: ['Teclado', 'Mouse', 'Monitor', 'Cámara', 'Parlantes']
#Ordenados: ['Cámara', 'Monitor', 'Mouse', 'Parlantes', 'Teclado']
#Lista después de sort(): ['Cámara', 'Monitor', 'Mouse', 'Parlantes', 'Teclado']