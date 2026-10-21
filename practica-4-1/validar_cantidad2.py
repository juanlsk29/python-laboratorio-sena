class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self._cantidad = cantidad  

producto = Producto("Camisa", 10)

try:
    entrada = input("Nueva cantidad: ")
    nueva_cantidad = int(entrada)
    
    if nueva_cantidad < 0:
        print("Cantidad inválida. La cantidad no puede ser negativa.")
    else:
        producto._cantidad = nueva_cantidad
        print(f"Cantidad actualizada de '{producto.nombre}': {producto._cantidad}")
        
except ValueError:
    print("Error: Por favor, introduce un número entero válido.")

#     PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-1> python validar_cantidad2.py
# Nueva cantidad: 5
# Cantidad actualizada de 'Camisa': 5