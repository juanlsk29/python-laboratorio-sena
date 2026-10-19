def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    return base * porcentaje / 100


precio = 100000
cantidad = 2
porcentaje_descuento = 10
porcentaje_impuesto = 19

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, porcentaje_descuento)
base_descuento = subtotal - descuento
impuesto = calcular_impuesto(base_descuento, porcentaje_impuesto)
total = base_descuento + impuesto

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Base después del descuento:", base_descuento)
print("Impuesto:", impuesto)
print("Total:", total)
