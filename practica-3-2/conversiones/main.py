from unidades import kilometros_a_metros, celsius_a_fahrenheit

kilometros = float(input("Ingrese la distancia en kilómetros: "))
celsius = float(input("Ingrese la temperatura en Celsius: "))

metros = kilometros_a_metros(kilometros)
fahrenheit = celsius_a_fahrenheit(celsius)

print("Distancia en metros:", metros)
print("Temperatura en Fahrenheit:", fahrenheit)

# PS C:\Users\PC\Desktop\python-laboratorio3> cd practica-3-2
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-2> cd conversiones
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-2\conversiones> python main.py
# Ingrese la distancia en kilómetros: 50
# Ingrese la temperatura en Celsius: 40
# Distancia en metros: 50000.0    
# Temperatura en Fahrenheit: 104.0