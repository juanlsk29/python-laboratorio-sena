producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0
}

print("Nombre:", producto.get("nombre"))
print("Marca:", producto.get("marca"))
print("Marca alternativa:", producto.get("marca", "Sin marca"))

#PS C:\Users\PC\Desktop\python-laboratorio2> python consultar_producto.py
#Nombre: Teclado
#Marca: None
#Marca alternativa: Sin marca