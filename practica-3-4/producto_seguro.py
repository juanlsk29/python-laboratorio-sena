# producto_seguro.py 1
# class Producto:
#     def __init__(self, codigo, nombre, precio, cantidad):
#         self._codigo = codigo
#         self._nombre = nombre
#         self._precio = precio
#         self._cantidad = cantidad

#     def calcular_valor(self):
#         return self._precio * self._cantidad

# producto = Producto("P001", "Teclado", 85000, 4)

# print(producto.calcular_valor())

# producto_seguro.py 2

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def calcular_valor(self):
        return self._precio * self._cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if nueva_cantidad < 0:
            return False

        self._cantidad = nueva_cantidad
        return True

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._precio = nuevo_precio


producto = Producto("P001", "Teclado", 85000, 4)

print("Código:", producto.codigo)
print("Nombre:", producto.nombre)
print("Cantidad inicial:", producto.cantidad)

print("Actualizar a 10:", producto.actualizar_existencias(10))
print("Cantidad actual:", producto.cantidad)

print("Actualizar a -5:", producto.actualizar_existencias(-5))
print("Cantidad después del rechazo:", producto.cantidad)

producto.precio = 90000
print("Nuevo precio:", producto.precio)

try:
    producto.precio = -5000
except ValueError as error:
    print("Error:", error)
