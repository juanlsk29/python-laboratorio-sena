CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

productos = []
opcion = ""

while opcion != "0":
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
    print("0. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría (Periféricos, Componentes, Accesorios): ").strip()

        if not codigo or not nombre or not categoria:
            print("Error: el código, nombre y categoría no pueden estar vacíos.")
            continue

       
        codigo_repetido = any(
            producto["codigo"] == codigo for producto in productos
        )

        if codigo_repetido:
            print("Error: ya existe un producto con ese código.")
            continue

        if categoria not in CATEGORIAS:
            print("Error: la categoría no está permitida.")
            continue

        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        if precio <= 0:
            print("Error: el precio debe ser mayor que cero.")
            continue

        if cantidad < 0:
            print("Error: la cantidad no puede ser negativa.")
            continue

        nuevo_producto = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad
        }

        productos.append(nuevo_producto)
        print("Producto registrado.")

    elif opcion == "2":
        if not productos:
            print("No hay productos registrados.")
        else:
            for producto in productos:
                print(
                    f'{producto["codigo"]} - {producto["nombre"]} - '
                    f'{producto["categoria"]} - ${producto["precio"]} - '
                    f'{producto["cantidad"]} unidades'
                )

    elif opcion == "3":
        codigo_buscado = input("Código del producto: ").strip()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is not None:
            print("Producto encontrado:")
            for clave, valor in encontrado.items():
                print(f"{clave}: {valor}")
        else:
            print("No se encontró el producto.")

    elif opcion == "4":
        codigo_buscado = input("Código del producto: ").strip()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("No se encontró el producto.")
        else:
            nueva_cantidad = int(input("Nueva cantidad disponible: "))

            if nueva_cantidad < 0:
                print("Error: la cantidad no puede ser negativa.")
            else:
                encontrado["cantidad"] = nueva_cantidad
                print("Existencias actualizadas.")

    elif opcion == "5":
        codigo_buscado = input("Código del producto a eliminar: ").strip()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("No se encontró el producto.")
        else:
            productos.remove(encontrado)
            print("Producto eliminado.")

    elif opcion == "6":
        agotados = [
            producto["nombre"]
            for producto in productos
            if producto["cantidad"] == 0
        ]

        if agotados:
            print("Sin existencias:")
            for nombre in agotados:
                print("-", nombre)
        else:
            print("No hay productos sin existencias.")

    elif opcion == "7":
        cantidad_productos = len(productos)
        unidades_totales = sum(
            producto["cantidad"] for producto in productos
        )
        valor_inventario = sum(
            producto["precio"] * producto["cantidad"]
            for producto in productos
        )
        categorias_utilizadas = {
            producto["categoria"] for producto in productos
        }

        print("Productos:", cantidad_productos)
        print("Unidades:", unidades_totales)
        print("Valor del inventario:", f"${valor_inventario}")
        print("Categorías utilizadas:", ", ".join(sorted(categorias_utilizadas))
              if categorias_utilizadas else "Ninguna")

    elif opcion == "0":
        print("Programa finalizado.")

    else:
        print("Opción no válida.")
