productos = [
    {"codigo": "P001", "nombre": "Teclado"},
    {"codigo": "P002", "nombre": "Mouse"},
    {"codigo": "P003", "nombre": "Monitor"}
]

catalogo = {
    producto["codigo"]: producto["nombre"]
    for producto in productos
}

print(catalogo)

#PS C:\Users\PC\Desktop\python-laboratorio2> python catalogo_por_codigo.py
#{'P001': 'Teclado', 'P002': 'Mouse', 'P003': 'Monitor'}