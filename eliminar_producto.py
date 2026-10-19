productos = ["Teclado", "Mouse", "Monitor"]

nombre = input("Producto a eliminar: ").strip()

if nombre in productos:
    productos.remove(nombre)
    print("Producto eliminado.")
else:
    print("No se encontró el producto.")

print("Lista actual:", productos)

#PS C:\Users\PC\Desktop\python-laboratorio2> python eliminar_producto.py
#Producto a eliminar: Monitor 
#Producto eliminado.
#Lista actual: ['Teclado', 'Mouse']