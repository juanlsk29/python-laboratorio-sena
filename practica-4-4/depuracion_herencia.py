class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Aprendiz(Persona):
    def __init__(self, nombre, ficha):
        super().__init__(nombre)
        self.ficha = ficha


aprendiz = Aprendiz("Juan", "123456")

print(aprendiz.nombre)
print(aprendiz.ficha)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-4> python depuracion_herencia.py
# Juan
# 123456