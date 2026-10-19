def agregar_en_copia(nombre, nombres):
    copia = nombres.copy()
    copia.append(nombre)
    return copia


original = ["Teclado"]
nueva = agregar_en_copia("Mouse", original)

print("Original:", original)
print("Nueva:", nueva)
