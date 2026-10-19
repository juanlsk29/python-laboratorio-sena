productos = [
    {"nombre": "Teclado", "categoria": "Periféricos"},
    {"nombre": "Mouse", "categoria": "Periféricos"},
    {"nombre": "Disco", "categoria": "Componentes"}
]

categorias = {
    producto["categoria"]
    for producto in productos
}

print(categorias)

#PS C:\Users\PC\Desktop\python-laboratorio2> python categorias_distintas.py
#{'Periféricos', 'Componentes'}