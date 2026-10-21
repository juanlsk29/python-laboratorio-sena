class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje


moto1 = Motocicleta("Yamaha", "MT-03", 321)
moto2 = Motocicleta("Honda", "CB190R", 184)

print("Motocicleta 1")
print("Marca:", moto1.marca)
print("Modelo:", moto1.modelo)
print("Cilindraje:", moto1.cilindraje, "cc")

print("\nMotocicleta 2")
print("Marca:", moto2.marca)
print("Modelo:", moto2.modelo)
print("Cilindraje:", moto2.cilindraje, "cc")

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-4> python vehiculos.py
# Motocicleta 1
# Marca: Yamaha
# Modelo: MT-03
# Cilindraje: 321 cc

# Motocicleta 2
# Marca: Honda
# Modelo: CB190R
# Cilindraje: 184 cc