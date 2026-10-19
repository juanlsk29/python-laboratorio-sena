grupos = [[1, 2], [3, 4], [5, 6]]

numeros = [
    numero
    for grupo in grupos
    for numero in grupo
]

print("Lista combinada:", numeros)

cuadrados = (numero ** 2 for numero in range(1, 5))

print("Tipo:", type(cuadrados))
print("Valores:", list(cuadrados))

tupla_cuadrados = tuple(
    numero ** 2 for numero in range(1, 5)
)

print("Tupla:", tupla_cuadrados)

#PS C:\Users\PC\Desktop\python-laboratorio2> python comprensiones_anidadas.py
#Lista combinada: [1, 2, 3, 4, 5, 6]
#Tipo: <class 'generator'>
#Valores: [1, 4, 9, 16]
#Tupla: (1, 4, 9, 16)