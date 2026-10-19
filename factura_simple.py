nombre_del_producto = "Camiseta"
precio_unitario = 100000
cantidad = 2
porcentaje_de_descuento = 0.10
impuesto = 0.25

subtotal = precio_unitario * cantidad
valor_de_descuento = subtotal * porcentaje_de_descuento
total = subtotal - valor_de_descuento

total_final = total * impuesto

print(f"Nombre: {nombre_del_producto}")
print(f"Precio: {precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Descuento: {porcentaje_de_descuento}")


print("Subtotal: $" + str(subtotal))
print("Descuento: $" + str(valor_de_descuento))
print(f"Impuesto: {impuesto}")
print("Total Parcial: $" + str(total))

print("Total Final: $" + str(total_final))