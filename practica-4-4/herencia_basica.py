class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def describir(self):
        return f"Empleado: {self.nombre}"


class Instructor(Empleado):
    def explicar(self):
        return f"{self.nombre} está orientando una actividad."


persona = Instructor("Juan")

print(persona.describir())
print(persona.explicar())

# PS C:\Users\PC\Desktop\python-laboratorio-4> cd practica-4-4
# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-4> python herencia_basica.py
# Empleado: Juan
# Juan está orientando una actividad.