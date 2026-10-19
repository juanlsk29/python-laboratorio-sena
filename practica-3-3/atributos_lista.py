# atributos_lista.py 1
# class Registro:
#     elementos = []


# primero = Registro()
# segundo = Registro()

# primero.elementos.append("Teclado")
# print(segundo.elementos)

# atributos_lista.py 2

class Registro:
    def __init__(self):
        self.elementos = []


primero = Registro()
segundo = Registro()

primero.elementos.append("Teclado")

print("Primero:", primero.elementos)
print("Segundo:", segundo.elementos)
