#V1
# from producto import Producto, CATEGORIAS
# from inventario import Inventario


# def leer_entero(mensaje, minimo=None):
#     while True:
#         try:
#             valor = int(input(mensaje))

#             if minimo is not None and valor < minimo:
#                 print(f"El valor debe ser mayor o igual que {minimo}.")
#                 continue

#             return valor

#         except ValueError:
#             print("Debes escribir un número entero válido.")


# def leer_precio():
#     while True:
#         try:
#             precio = float(input("Precio unitario: "))

#             if precio <= 0:
#                 print("El precio debe ser mayor que cero.")
#                 continue

#             return precio

#         except ValueError:
#             print("Debes escribir un precio numérico válido.")


# def mostrar_producto(producto):
#     print(f"Código: {producto.codigo}")
#     print(f"Nombre: {producto.nombre}")
#     print(f"Categoría: {producto.categoria}")
#     print(f"Precio unitario: ${producto.precio:,.2f}")
#     print(f"Cantidad disponible: {producto.cantidad}")
#     print(f"Valor de existencias: ${producto.calcular_valor():,.2f}")


# def registrar_producto(inventario):
#     print("\n--- Registrar producto ---")

#     codigo = input("Código: ")
#     nombre = input("Nombre: ")

#     print("\nCategorías permitidas:")
#     for indice, categoria in enumerate(CATEGORIAS, start=1):
#         print(f"{indice}. {categoria}")

#     opcion = leer_entero("Selecciona una categoría: ", 1)

#     if opcion > len(CATEGORIAS):
#         print("La categoría seleccionada no existe.")
#         return

#     categoria = CATEGORIAS[opcion - 1]
#     precio = leer_precio()
#     cantidad = leer_entero("Cantidad disponible: ", 0)

#     try:
#         producto = Producto(
#             codigo,
#             nombre,
#             categoria,
#             precio,
#             cantidad
#         )

#         if inventario.registrar_producto(producto):
#             print("Producto registrado correctamente.")
#         else:
#             print("Ya existe un producto con ese código.")

#     except ValueError as error:
#         print(f"No se pudo registrar el producto: {error}")


# def listar_productos(inventario):
#     print("\n--- Lista de productos ---")
#     productos = inventario.listar_productos()

#     if not productos:
#         print("No hay productos registrados.")
#         return

#     for producto in productos:
#         print("\n------------------------------")
#         mostrar_producto(producto)


# def buscar_producto(inventario):
#     print("\n--- Buscar producto ---")
#     codigo = input("Código del producto: ")
#     producto = inventario.buscar_por_codigo(codigo)

#     if producto is None:
#         print("Producto no registrado.")
#     else:
#         mostrar_producto(producto)


# def actualizar_existencias(inventario):
#     print("\n--- Actualizar existencias ---")
#     codigo = input("Código del producto: ")

#     producto = inventario.buscar_por_codigo(codigo)

#     if producto is None:
#         print("Producto no registrado.")
#         return

#     nueva_cantidad = leer_entero("Nueva cantidad: ", 0)

#     if inventario.actualizar_existencias(codigo, nueva_cantidad):
#         print("Existencias actualizadas correctamente.")
#     else:
#         print("No fue posible actualizar las existencias.")


# def eliminar_producto(inventario):
#     print("\n--- Eliminar producto ---")
#     codigo = input("Código del producto: ")

#     if inventario.eliminar_producto(codigo):
#         print("Producto eliminado correctamente.")
#     else:
#         print("No existe un producto con ese código.")


# def mostrar_productos_sin_stock(inventario):
#     print("\n--- Productos sin stock ---")
#     productos = inventario.productos_sin_stock()

#     if not productos:
#         print("No hay productos sin stock.")
#         return

#     for producto in productos:
#         print(f"{producto.codigo} - {producto.nombre}")


# def mostrar_resumen(inventario):
#     print("\n--- Resumen del inventario ---")
#     datos = inventario.resumen()

#     print("Productos diferentes:", datos["productos_diferentes"])
#     print("Unidades disponibles:", datos["unidades_disponibles"])
#     print(f"Valor total: ${datos['valor_total']:,.2f}")

#     if datos["categorias"]:
#         print("Categorías utilizadas:")
#         for categoria in sorted(datos["categorias"]):
#             print(f"- {categoria}")
#     else:
#         print("Categorías utilizadas: ninguna")


# def mostrar_menu():
#     print("\n================================")
#     print("       GESTOR DE INVENTARIO")
#     print("================================")
#     print("1. Registrar producto")
#     print("2. Listar productos")
#     print("3. Buscar por código")
#     print("4. Actualizar existencias")
#     print("5. Eliminar producto")
#     print("6. Consultar productos sin stock")
#     print("7. Resumen del inventario")
#     print("0. Salir")


# def main():
#     inventario = Inventario()

#     while True:
#         mostrar_menu()
#         opcion = input("Selecciona una opción: ").strip()

#         if opcion == "1":
#             registrar_producto(inventario)
#         elif opcion == "2":
#             listar_productos(inventario)
#         elif opcion == "3":
#             buscar_producto(inventario)
#         elif opcion == "4":
#             actualizar_existencias(inventario)
#         elif opcion == "5":
#             eliminar_producto(inventario)
#         elif opcion == "6":
#             mostrar_productos_sin_stock(inventario)
#         elif opcion == "7":
#             mostrar_resumen(inventario)
#         elif opcion == "0":
#             print("Programa finalizado.")
#             break
#         else:
#             print("Opción no válida. Intenta nuevamente.")


# if __name__ == "__main__":
#     main()


# RESULTADO:
# PS C:\Users\PC\Desktop\python-laboratorio3> cd gestor_inventario
# PS C:\Users\PC\Desktop\python-laboratorio3\gestor_inventario> python main.py

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
# 0. Salir
# Selecciona una opción: 1

# --- Registrar producto ---
# Código: P001
# Nombre: Teclado

# Categorías permitidas:
# 1. Periféricos
# 2. Componentes
# 3. Accesorios
# Selecciona una categoría: Perifericos
# Debes escribir un número entero válido.
# Selecciona una categoría: 1
# Precio unitario: 85000
# Cantidad disponible: 4
# Producto registrado correctamente.

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
# 0. Salir
# Selecciona una opción: 1

# --- Registrar producto ---
# Código: P002 
# Nombre: Mouse

# Categorías permitidas:
# 1. Periféricos
# 2. Componentes
# 3. Accesorios
# Selecciona una categoría: 1
# Precio unitario: 45000
# Cantidad disponible: 0
# Producto registrado correctamente.

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
# 0. Salir
# Selecciona una opción: 7

# --- Resumen del inventario ---
# Productos diferentes: 2
# Unidades disponibles: 4
# Valor total: $340,000.00
# Categorías utilizadas:
# - Periféricos



# V2
from producto import Producto, CATEGORIAS
from inventario import Inventario


def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Debes escribir un número entero.")
            continue

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue

        return cantidad


def leer_precio():
    while True:
        try:
            precio = float(input("Precio: "))
        except ValueError:
            print("Debes escribir un número válido.")
            continue

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue

        return precio


def mostrar_producto(producto):
    print(
        f"{producto.codigo} - {producto.nombre} - "
        f"{producto.categoria} - ${producto.precio} - "
        f"{producto.cantidad} unidades"
    )


def registrar_producto(inventario):
    print("\n--- Registrar producto ---")

    codigo = input("Código: ")
    nombre = input("Nombre: ")

    print("Categorías:")
    for numero, categoria in enumerate(CATEGORIAS, start=1):
        print(f"{numero}. {categoria}")

    try:
        opcion_categoria = int(input("Selecciona una categoría: "))
    except ValueError:
        print("Debes introducir un número de categoría.")
        return

    if not 1 <= opcion_categoria <= len(CATEGORIAS):
        print("Categoría no válida.")
        return

    categoria = CATEGORIAS[opcion_categoria - 1]
    precio = leer_precio()
    cantidad = leer_cantidad()

    try:
        producto = Producto(
            codigo, nombre, categoria, precio, cantidad
        )
    except ValueError as error:
        print(f"No se pudo registrar: {error}")
        return

    if inventario.registrar_producto(producto):
        print("Producto registrado.")
    else:
        print("Ya existe un producto con ese código.")


def listar_productos(inventario):
    productos = inventario.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        mostrar_producto(producto)


def buscar_producto(inventario):
    codigo = input("Código: ")
    producto = inventario.buscar_por_codigo(codigo)

    if producto is None:
        print("El producto no existe.")
    else:
        mostrar_producto(producto)


def actualizar_producto(inventario):
    codigo = input("Código: ")

    if inventario.buscar_por_codigo(codigo) is None:
        print("El producto no existe.")
        return

    print("Introduce la nueva cantidad.")
    cantidad = leer_cantidad()

    if inventario.actualizar_existencias(codigo, cantidad):
        print("Existencias actualizadas.")
    else:
        print("No se pudieron actualizar las existencias.")


def eliminar_producto(inventario):
    codigo = input("Código: ")

    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("El producto no existe.")


def mostrar_sin_stock(inventario):
    agotados = inventario.productos_sin_stock()

    if not agotados:
        print("No hay productos sin stock.")
        return

    print("Sin existencias:")
    for producto in agotados:
        print(f"- {producto.nombre}")


def mostrar_resumen(inventario):
    datos = inventario.resumen()

    print("Productos registrados:", datos["productos_registrados"])
    print("Unidades disponibles:", datos["unidades_disponibles"])
    print(f"Valor del inventario: ${datos['valor_total']}")
    print("Categorías utilizadas:", len(datos["categorias"]))

    if datos["categorias"]:
        print("Categorías:", ", ".join(sorted(datos["categorias"])))


def mostrar_menu():
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Buscar productos por categoría")
    print("9. Listar productos ordenados por nombre")
    print("10. Actualizar precio")
    print("11. Mostrar producto de mayor valor")
    print("12. Mostrar diccionario de productos")
    print("0. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            listar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            actualizar_producto(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            mostrar_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "8":
            buscar_categoria(inventario)
        elif opcion == "9":
            listar_ordenados(inventario)
        elif opcion == "10":
            cambiar_precio(inventario)
        elif opcion == "11":
            mostrar_mayor_valor(inventario)
        elif opcion == "12":
            mostrar_diccionario(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

# RESULTADOS V2
# PS C:\Users\PC\Desktop\python-laboratorio3> cd gestor_inventario
# PS C:\Users\PC\Desktop\python-laboratorio3\gestor_inventario> python main.py

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
# 0. Salir
# Opción: 1

# --- Registrar producto ---
# Código: P001
# Nombre: Teclado
# Categorías:
# 1. Periféricos
# 2. Componentes
# 3. Accesorios
# Selecciona una categoría: 1 
# Precio: 85000
# Cantidad: 4
# Producto registrado.

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
# 0. Salir
# Opción: 1

# --- Registrar producto ---
# Código: P002
# Nombre: Mouse
# Categorías:
# 1. Periféricos
# 2. Componentes
# 3. Accesorios
# Selecciona una categoría: 1
# Precio: 45000
# Cantidad: 0
# Producto registrado.

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
# 0. Salir
# Opción: 1

# --- Registrar producto ---
# Código: P003
# Nombre: Procesador
# Categorías:
# 1. Periféricos
# 2. Componentes
# 3. Accesorios
# Selecciona una categoría: 2
# Precio: 700000
# Cantidad: 2
# Producto registrado.

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
# 0. Salir
# Opción: 7
# Productos registrados: 3
# Unidades disponibles: 6
# Valor del inventario: $1740000.0
# Categorías utilizadas: 2
# Categorías: Componentes, Periféricos

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
# 0. Salir
# Opción: 4
# Código: P002
# Introduce la nueva cantidad.
# Cantidad: 5
# Existencias actualizadas.

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
# 0. Salir
# Opción: 0
# Programa finalizado.

# NUEVO RETO 19
def buscar_categoria(inventario):
    print("Categorías:")
    for numero, categoria in enumerate(CATEGORIAS, start=1):
        print(f"{numero}. {categoria}")

    try:
        opcion = int(input("Selecciona una categoría: "))
    except ValueError:
        print("Opción no válida.")
        return

    if not 1 <= opcion <= len(CATEGORIAS):
        print("Categoría no válida.")
        return

    categoria = CATEGORIAS[opcion - 1]
    productos = inventario.buscar_por_categoria(categoria)

    if not productos:
        print("No hay productos en esa categoría.")
        return

    for producto in productos:
        mostrar_producto(producto)


def listar_ordenados(inventario):
    productos = inventario.listar_ordenados_por_nombre()

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        mostrar_producto(producto)


def cambiar_precio(inventario):
    codigo = input("Código del producto: ")

    try:
        precio = float(input("Nuevo precio: "))
    except ValueError:
        print("Debes introducir un precio numérico.")
        return

    if inventario.actualizar_precio(codigo, precio):
        print("Precio actualizado correctamente.")
    else:
        print("No se pudo actualizar. Verifica el código y el precio.")


def mostrar_mayor_valor(inventario):
    producto = inventario.producto_mayor_valor()

    if producto is None:
        print("No hay productos registrados.")
        return

    print("Producto con mayor valor de inventario:")
    mostrar_producto(producto)
    print(f"Valor total: ${producto.calcular_valor()}")


def mostrar_diccionario(inventario):
    productos = inventario.diccionario_productos()
    print(productos)