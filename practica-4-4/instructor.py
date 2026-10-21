class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre


class Instructor(Empleado):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad


instructor = Instructor("Juan", "Python")

print(instructor.nombre)
print(instructor.especialidad)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-4> python instructor.py
# Juan
# Python