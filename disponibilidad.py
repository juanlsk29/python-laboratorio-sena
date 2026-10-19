unidades_disponibles = 12
unidades_solicitadas = 15

hay_suficientes = unidades_solicitadas <= unidades_disponibles
cantidades_iguales = unidades_solicitadas == unidades_disponibles
mas_solicitadas = unidades_solicitadas > unidades_disponibles


print(f"Disponibles: {unidades_disponibles} | Solicitadas: {unidades_solicitadas}")
print(f" ¿Hay suficientes unidades?: {hay_suficientes}")
print(f" ¿Las cantidades son iguales?: {cantidades_iguales}")
print(f" ¿Se solicitaron más unidades de las disponibles?: {mas_solicitadas}")

#Disponibles: 12 | Solicitadas: 8
# ¿Hay suficientes unidades?: True
# ¿Las cantidades son iguales?: False
# ¿Se solicitaron más unidades de las disponibles?: False

#Disponibles: 12 | Solicitadas: 12
# ¿Hay suficientes unidades?: True
# ¿Las cantidades son iguales?: True
# ¿Se solicitaron más unidades de las disponibles?: False

#Disponibles: 12 | Solicitadas: 15
# ¿Hay suficientes unidades?: False
# ¿Las cantidades son iguales?: False
# ¿Se solicitaron más unidades de las disponibles?: True