nombre_cliente = "Juan"
precio_unitario = 50000
cantidad = 2

# ERROR 1: Error de sintaxis

# CORRECCIÓN 1: Agregar las comillas faltantes al final de la cadena.
print("Iniciando cotización...")

subtotal = precio_unitario * cantidad

# ERROR 2: Variable inexistente 
# total_impuesto = sub_total * 0.19

# CORRECCIÓN 2: Utilizar el nombre de variable correcto 
total_impuesto = subtotal * 0.19

# ERROR 3: Cálculo lógicamente incorrecto (se calcula el impuesto sobre el precio unitario en vez del subtotal)
# impuesto_incorrecto = precio_unitario * 0.19

# CORRECCIÓN 3: Aplicar el porcentaje de impuesto sobre la base o subtotal correspondiente
impuesto_correcto = subtotal * 0.19