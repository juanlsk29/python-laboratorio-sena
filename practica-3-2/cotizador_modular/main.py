from calculos import (
    calcular_subtotal,
    calcular_descuento,
    calcular_impuesto
)
from validaciones import (
    precio_valido,
    cantidad_valida,
    porcentaje_valido
)


def ejecutar_cotizador():
    precio = float(input("Ingrese el precio: "))
    cantidad = float(input("Ingrese la cantidad: "))
    descuento_porcentaje = float(input("Ingrese el descuento (%): "))
    impuesto_porcentaje = float(input("Ingrese el impuesto (%): "))

    if not precio_valido(precio):
        print("Error: el precio debe ser mayor que cero.")
        return

    if not cantidad_valida(cantidad):
        print("Error: la cantidad debe ser un entero positivo.")
        return

    if not porcentaje_valido(descuento_porcentaje):
        print("Error: el descuento debe estar entre 0 y 100.")
        return

    if not porcentaje_valido(impuesto_porcentaje):
        print("Error: el impuesto debe estar entre 0 y 100.")
        return

    subtotal = calcular_subtotal(precio, int(cantidad))
    descuento = calcular_descuento(subtotal, descuento_porcentaje)
    base = subtotal - descuento
    impuesto = calcular_impuesto(base, impuesto_porcentaje)
    total = base + impuesto

    print("Subtotal:", subtotal)
    print("Descuento:", descuento)
    print("Base después del descuento:", base)
    print("Impuesto:", impuesto)
    print("Total:", total)


if __name__ == "__main__":
    ejecutar_cotizador()

# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-2\cotizador_modular> python main.py
# Ingrese el precio: 100000
# Ingrese la cantidad: 2
# Ingrese el descuento (%): 10
# Ingrese el impuesto (%): 19
# Subtotal: 200000.0
# Descuento: 20000.0
# Base después del descuento: 180000.0
# Impuesto: 34200.0
# Total: 214200.0

# PS C:\Users\PC\Desktop\python-laboratorio3> cd practica-3-2     
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-2> cd cotizador_modular
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-2\cotizador_modular> python -c "import calculos; print('Módulo importado correctamente')"
# Módulo importado correctamente