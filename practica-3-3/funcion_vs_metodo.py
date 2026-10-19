def calcular_valor(precio, cantidad):
    return precio * cantidad


class Producto:
    def __init__(self, precio, cantidad):
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor(self):
        return self.precio * self.cantidad


print("Con función:", calcular_valor(85000, 4))

teclado = Producto(85000, 4)
print("Con método:", teclado.calcular_valor())
