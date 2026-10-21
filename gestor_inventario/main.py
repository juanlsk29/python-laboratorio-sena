from producto import Producto, CATEGORIAS
from inventario import Inventario
from almacenamiento import (
    cargar_inventario,
    guardar_inventario,
    ErrorCargaInventario
)
from reportes import exportar_csv


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"El valor debe ser como mínimo {minimo}.")
                continue

            return valor
        except ValueError:
            print("Entrada inválida. Escribe un número entero.")


def leer_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje))

            # La validación definitiva también se realiza en Producto.
            import math
            if not math.isfinite(valor) or valor <= 0:
                print("El precio debe ser positivo y finito.")
                continue

            return valor
        except ValueError:
            print("Precio inválido. Escribe un número válido.")


def mostrar_menu():
    print("\n================================")
    print("        GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Guardar inventario")
    print("9. Exportar reporte CSV")
    print("0. Salir")


def guardar_cambios(inventario):
    try:
        ruta = guardar_inventario(inventario)
        print("Inventario guardado correctamente:", ruta)
    except OSError as error:
        print(error)
        print("Los cambios podrían existir solamente en memoria.")


try:
    inventario = cargar_inventario()
    solo_lectura = False
    print("Inventario cargado correctamente.")
    print("Productos recuperados:", len(inventario.listar()))

except ErrorCargaInventario as error:
    inventario = Inventario()
    solo_lectura = True
    print("\nATENCIÓN:", error)
    print("El archivo original está protegido.")
    print("Las modificaciones y el guardado están bloqueados.")
    print("Corrige o recupera el archivo antes de continuar.")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        if solo_lectura:
            print("No se puede modificar el inventario.")
            continue

        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()

        # Selección de categoría mediante texto directo
        categoria = input(
            "Categoría (Periféricos, Componentes, Accesorios): "
        ).strip()

        if categoria not in CATEGORIAS:
            print("Categoría inválida.")
            continue

        precio = leer_precio("Precio: ")
        cantidad = leer_entero("Cantidad: ", 0)

        try:
            producto = Producto(
                codigo, nombre, categoria, precio, cantidad
            )
            inventario.registrar(producto)
            print("Producto registrado.")
            guardar_cambios(inventario)
        except ValueError as error:
            print("No se pudo registrar:", error)

    elif opcion == "2":
        productos = inventario.listar()

        if not productos:
            print("No hay productos para mostrar.")
        else:
            for producto in productos:
                print(producto)

    elif opcion == "3":
        codigo = input("Código que deseas buscar: ").strip()
        producto = inventario.buscar(codigo)

        if producto is None:
            print("Producto no encontrado.")
        else:
            print(producto)

    elif opcion == "4":
        if solo_lectura:
            print("No se puede modificar el inventario.")
            continue

        codigo = input("Código del producto: ").strip()
        cantidad = leer_entero("Nueva cantidad: ", 0)

        try:
            inventario.actualizar_existencias(codigo, cantidad)
            print("Existencias actualizadas.")
            guardar_cambios(inventario)
        except ValueError as error:
            print("No se pudo actualizar:", error)

    elif opcion == "5":
        if solo_lectura:
            print("No se puede modificar el inventario.")
            continue

        codigo = input("Código del producto que deseas eliminar: ").strip()

        try:
            inventario.eliminar(codigo)
            print("Producto eliminado.")
            guardar_cambios(inventario)
        except ValueError as error:
            print("No se pudo eliminar:", error)

    elif opcion == "6":
        productos = inventario.productos_sin_stock()

        if not productos:
            print("No hay productos sin stock.")
        else:
            for producto in productos:
                print(producto)

    elif opcion == "7":
        resumen = inventario.resumen()
        print("Productos registrados:", resumen["productos"])
        print("Unidades disponibles:", resumen["unidades"])
        print(f"Valor total del inventario: ${resumen['valor_total']:.2f}")

    elif opcion == "8":
        if solo_lectura:
            print("Guardado bloqueado para proteger el archivo dañado.")
        else:
            guardar_cambios(inventario)

    elif opcion == "9":
        try:
            ruta = exportar_csv(inventario)
            print("Reporte exportado correctamente:", ruta)
        except OSError as error:
            print(error)

    elif opcion == "0":
        print("Finalizando gestor de inventario.")
        break

    else:
        print("Opción inválida. Intenta nuevamente.")


# EVIDENCIAS 
#1
# El menu aparece con el json no existente en datos
# PS C:\Users\PC\Desktop\python-laboratorio-4\gestor_inventario> python main.py
# Inventario cargado correctamente.
# Productos recuperados: 0

# ================================
#        GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir

#2 
# NO se permite crear un producto de mismo codigo
# PS C:\Users\PC\Desktop\python-laboratorio-4\gestor_inventario> python main.py
# Inventario cargado correctamente.
# Productos recuperados: 3

# ================================
#        GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 1
# Código: P001
# Nombre: Teclado
# Categorías disponibles:
# 1. Periféricos
# 2. Componentes
# 3. Accesorios
# Selecciona la categoría: 1
# Precio: 85000
# Cantidad: 4
# No se pudo registrar: Ya existe un producto con ese código.

#3 
# No se permiten otras categorias 
# PS C:\Users\PC\Desktop\python-laboratorio-4\gestor_inventario> python main.py
# Inventario cargado correctamente.
# Productos recuperados: 3

# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 1
# Código: P004
# Nombre: Agua
# Categoría (Periféricos, Componentes, Accesorios): Juguetes
# Categoría inválida.

#4 
# El programa rechaza precios por debajo de cero
# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 1
# Código: P005
# Nombre: Agua
# Categoría (Periféricos, Componentes, Accesorios): Componentes
# Precio: -100
# El precio debe ser positivo y finito.
# Precio: nan
# El precio debe ser positivo y finito.
# Precio: inf
# El precio debe ser positivo y finito.

#5
# No se permiten cantidades por debajo de cero

# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 1
# Código: P006
# Nombre: Espada
# Categoría (Periféricos, Componentes, Accesorios): Accesorios 
# Precio: 5000
# Cantidad: -3
# El valor debe ser como mínimo 0.
# Cantidad: 1
# Producto registrado.

#6
#Es posible guardar un producto con cantidad 0 y este aparece en opcion 6
# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 1
# Código: P007
# Nombre: Ram8
# Categoría (Periféricos, Componentes, Accesorios): Componentes
# Precio: 90000
# Cantidad: 0
# Producto registrado.
# Inventario guardado correctamente: C:\Users\PC\Desktop\python-laboratorio-4\gestor_inventario\datos\productos.json

# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 6
# P007 | Ram8 | Componentes | $90000.00 | Cantidad: 0


#7 
# Si se pone un precio o una cantidad no valida el programa deja volver a intentarlo
# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 6
# P007 | Ram8 | Componentes | $90000.00 | Cantidad: 0

# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 1
# Código: P008
# Nombre: Leche
# Categoría (Periféricos, Componentes, Accesorios): Accesorios
# Precio: abc
# Precio inválido. Escribe un número válido.
# Precio: 20000
# Cantidad: hola
# Entrada inválida. Escribe un número entero.
# Cantidad: 2
# Producto registrado.
# Inventario guardado correctamente: C:\Users\PC\Desktop\python-laboratorio-4\gestor_inventario\datos\productos.json

#8 
# El programa no funciona si el JSON esta vacio 

# El archivo original está protegido.
# Las modificaciones y el guardado están bloqueados.
# Corrige o recupera el archivo antes de continuar.

# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 8
# Guardado bloqueado para proteger el archivo dañado.

#9
# Codigos repetidos en el JSON

# PS C:\Users\PC\Desktop\python-laboratorio-4\gestor_inventario> python main.py

# ATENCIÓN: No se pudo recuperar productos.json: Ya existe un producto con ese código.
# El archivo original está protegido.
# Las modificaciones y el guardado están bloqueados.
# Corrige o recupera el archivo antes de continuar.

#10 
# El sistema genera un error al no existir un archivo de datos donde guardar

# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 1
# Código: P001
# Nombre: Juan
# Categoría (Periféricos, Componentes, Accesorios): Componentes
# Precio: 5000
# Cantidad: 5
# Producto registrado.
# [WinError 183] No se puede crear un archivo que ya existe: 'C:\\Users\\PC\\Desktop\\python-laboratorio-4\\gestor_inventario\\datos'
# Los cambios podrían existir solamente en memoria.

#11
# El sistema al dar en 0 se cierra correctamente 
# PS C:\Users\PC\Desktop\python-laboratorio-4\gestor_inventario> python main.py
# Inventario cargado correctamente.
# Productos recuperados: 7

# ================================
#         GESTOR DE INVENTARIO
# ================================
# 1. Registrar producto
# 2. Listar productos
# 3. Buscar por código
# 4. Actualizar existencias
# 5. Eliminar producto
# 6. Consultar productos sin stock
# 7. Resumen del inventario
# 8. Guardar inventario
# 9. Exportar reporte CSV
# 0. Salir
# Selecciona una opción: 0
# Finalizando gestor de inventario.
# PS C:\Users\PC\Desktop\python-laboratorio-4\gestor_inventario> 