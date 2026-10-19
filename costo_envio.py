compra = float(input("Cuanto fue tu compra? "))
 
if compra >= 200000: 
    envio = 0
elif compra >= 100000:
    envio = 10000
else:
    envio = 18000

total = compra + envio
print("=========================")
print("     RESUMEN DE CUENTA")
print("=========================")
print(f"Valor de la compra:", compra)
print(f"Costo de Envio", envio)
print(f"Total de la compra", total)
