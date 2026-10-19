productos = ["Teclado", "Mouse", "Monitor"]

buscado = input("Buscar producto: ").strip()

if buscado in productos:
    print("Producto encontrado.")
else:
    print("Producto no registrado.")

#PS C:\Users\PC\Desktop\python-laboratorio2> python buscar_producto.py
#Buscar producto: Mouse
#Producto encontrado.
#PS C:\Users\PC\Desktop\python-laboratorio2> python buscar_producto.py
#Buscar producto: Agua
#Producto no registrado.