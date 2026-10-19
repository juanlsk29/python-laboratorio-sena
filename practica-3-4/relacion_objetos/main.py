# main.py 1
# from producto import Producto
# from inventario import Inventario

# inventario = Inventario()

# inventario.agregar(Producto("P001", "Teclado"))
# inventario.agregar(Producto("P002", "Mouse"))

# for producto in inventario.listar():
#     print(producto.codigo, "-", producto.nombre)

# RESULTADO:
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-4> cd relacion_objetos
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-4\relacion_objetos> python main.py
# P001 - Teclado
# P002 - Mouse

# main.py 2 

from producto import Producto
from inventario import Inventario

inventario = Inventario()

inventario.agregar(Producto("P001", "Teclado"))
inventario.agregar(Producto("P002", "Mouse"))

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

encontrado = inventario.buscar_por_codigo("P002")

if encontrado is not None:
    print("Encontrado:", encontrado.nombre)
else:
    print("Producto no registrado.")

# RESULTADO: 
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-4\relacion_objetos> python main.py
# P001 - Teclado
# P002 - Mouse
# Encontrado: Mouse