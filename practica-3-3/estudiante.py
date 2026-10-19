class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print("Nombre:", self.nombre)
        print("Ficha:", self.ficha)
        print("Promedio:", self.promedio)

    def aprobo(self):
        return self.promedio >= 3.0


estudiante1 = Estudiante("Juan", "3388087", 2.8)
estudiante2 = Estudiante("Kevin", "3388087", 4.1)

estudiante1.mostrar_perfil()
print("¿Aprobó?", estudiante1.aprobo())

print()

estudiante2.mostrar_perfil()
print("¿Aprobó?", estudiante2.aprobo())
