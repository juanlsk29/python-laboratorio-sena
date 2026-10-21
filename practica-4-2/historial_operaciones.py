from pathlib import Path

ruta = Path(__file__).resolve().parent / "operaciones.txt"

while True:
    print("\n1. Registrar operación")
    print("2. Mostrar historial")
    print("0. Salir")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        concepto = input("Concepto: ").strip()

        try:
            valor = float(input("Valor: "))
        except ValueError:
            print("Error: debes ingresar un valor numérico.")
            continue

        if not concepto:
            print("Error: el concepto no puede estar vacío.")
            continue

        with ruta.open("a", encoding="utf-8") as archivo:
            archivo.write(f"{concepto} | {valor}\n")

        print("Operación registrada correctamente.")

    elif opcion == "2":
        try:
            with ruta.open("r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            if contenido.strip():
                print("\nHistorial de operaciones:")
                print(contenido)
            else:
                print("El historial está vacío.")

        except FileNotFoundError:
            print("Todavía no hay operaciones registradas.")

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida. Intenta nuevamente.")

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python historial_operaciones.py

# 1. Registrar operación
# 2. Mostrar historial
# 0. Salir
# Selecciona una opción: 1
# Concepto: Compra teclado
# Valor: 85000
# Operación registrada correctamente.

# 1. Registrar operación
# 2. Mostrar historial
# 0. Salir
# Selecciona una opción: 2

# Historial de operaciones:
# Compra teclado | 85000.0


# 1. Registrar operación
# 2. Mostrar historial
# 0. Salir
# Selecciona una opción: 0
# Programa finalizado.