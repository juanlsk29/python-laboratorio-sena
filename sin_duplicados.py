productos = ["Teclado", "Mouse"]

nombre = input("Ingrese un producto nuevo: ").strip()

if nombre == "":
    print("El producto no puede estar vacío.")
elif nombre in productos:
    print("El producto ya está registrado.")
else:
    productos.append(nombre)
    print("Producto registrado correctamente.")

print("Lista de productos:", productos)

#PS C:\Users\PC\Desktop\python-laboratorio2> python sin_duplicados.py
#Ingrese un producto nuevo: Agua
#Producto registrado correctamente.
#Lista de productos: ['Teclado', 'Mouse', 'Agua']
#PS C:\Users\PC\Desktop\python-laboratorio2> python sin_duplicados.py
#Ingrese un producto nuevo: Mouse
#El producto ya está registrado.
#Lista de productos: ['Teclado', 'Mouse']