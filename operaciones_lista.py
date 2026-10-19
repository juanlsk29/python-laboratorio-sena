productos = ["Teclado", "Mouse", "Monitor"]

productos[1] = "Mouse inalámbrico"
productos.insert(1, "Cámara web")

eliminado = productos.pop()

print("Elementos:", productos)
print("Extraído:", eliminado)

#PS C:\Users\PC\Desktop\python-laboratorio2> python operaciones_lista.py
#Elementos: ['Teclado', 'Cámara web', 'Mouse inalámbrico']
#Extraído: Monitor