productos = ["Teclado", "Mouse", "Monitor"]
nuevos = ["Impresora", "Cámara"]

# 1. Reemplazar Mouse
productos[1] = "Mouse inalámbrico"
print("Paso 1:", productos)

# 2. Insertar Parlantes en la primera posición
productos.insert(0, "Parlantes")
print("Paso 2:", productos)

# 3. Agregar los nuevos productos
productos.extend(nuevos)
print("Paso 3:", productos)

# 4. Eliminar Monitor
productos.remove("Monitor")
print("Paso 4:", productos)

# 5. Extraer el último elemento
extraido = productos.pop()
print("Paso 5:", productos)
print("Elemento extraído:", extraido)

#PS C:\Users\PC\Desktop\python-laboratorio2> python cambios_inventario.py
#Paso 1: ['Teclado', 'Mouse inalámbrico', 'Monitor']
#Paso 2: ['Parlantes', 'Teclado', 'Mouse inalámbrico', 'Monitor']
#Paso 3: ['Parlantes', 'Teclado', 'Mouse inalámbrico', 'Monitor', 'Impresora', 'Cámara']
#Paso 4: ['Parlantes', 'Teclado', 'Mouse inalámbrico', 'Impresora', 'Cámara']
#Paso 5: ['Parlantes', 'Teclado', 'Mouse inalámbrico', 'Impresora']
#Elemento extraído: Cámara