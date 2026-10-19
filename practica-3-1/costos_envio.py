def calcular_cobro(valor_compra, envio=10000):
    return valor_compra + envio


print("Compra con envío:", calcular_cobro(50000))
print("Compra con envío gratuito:", calcular_cobro(50000, 0))
