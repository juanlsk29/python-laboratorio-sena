aprendiz = {
    "ficha": "3388087",
    "nombre": "Juan",
    "trimestre": 6,
    "promedio": 4.2,
    "activo": True
}

print("Nombre:", aprendiz["nombre"])

aprendiz["trimestre"] = 3
aprendiz["correo"] = "aprendiz@example.com"

print("Perfil actualizado:")
print(aprendiz)

#PS C:\Users\PC\Desktop\python-laboratorio2> python perfil_diccionario.py
#Nombre: Juan
#Perfil actualizado:
#{'ficha': '3388087', 'nombre': 'Juan', 'trimestre': 3, 'promedio': 4.2, 'activo': True, 'correo': 'aprendiz@example.com'}