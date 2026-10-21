import json


class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"]
        )


producto = Producto("P001", "Teclado")

try:
    print(json.dumps(producto))
except TypeError:
    print("No se puede convertir directamente el objeto a JSON.")

texto = json.dumps(producto.a_diccionario(), ensure_ascii=False)
print(texto)

datos = {"codigo": "P002", "nombre": "Mouse"}
nuevo = Producto.desde_diccionario(datos)

print(type(nuevo))
print(nuevo.nombre)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python producto_json.py
# No se puede convertir directamente el objeto a JSON.
# {"codigo": "P001", "nombre": "Teclado"}
# <class '__main__.Producto'>
# Mouse