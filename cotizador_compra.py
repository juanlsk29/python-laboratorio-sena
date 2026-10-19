codigo_cotizacion = input("Código de cotización: ")
nombre_vendedor = input("Nombre del vendedor: ")
nombre_cliente = input("Nombre del cliente: ")
nombre_producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Descuento (%): "))
porcentaje_impuesto = input("Impuesto (%): ")
porcentaje_impuesto = float(porcentaje_impuesto) if porcentaje_impuesto else 0.0
costo_envio = float(input("Costo de envío: "))

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * (porcentaje_descuento / 100)
base = subtotal - valor_descuento
valor_impuesto = base * (porcentaje_impuesto / 100)
total_parcial = base + valor_impuesto
total = total_parcial + costo_envio

print("\n" + "=" * 29)
print("      COTIZADOR PYTHON")
print("=" * 29)
print(f"Código de cotización: {codigo_cotizacion}")
print(f"Vendedor: {nombre_vendedor}")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")

print("\n-----------------------------")
print("RESUMEN DE COMPRA")
print("-----------------------------")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"Costo de envío: ${costo_envio}")
print(f"TOTAL: ${total}")