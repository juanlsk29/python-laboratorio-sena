#V1
# class Inventario:
#     def __init__(self):
#         self._productos = []

#     def registrar_producto(self, producto):
#         if self.buscar_por_codigo(producto.codigo) is not None:
#             return False

#         self._productos.append(producto)
#         return True

#     def listar_productos(self):
#         return self._productos.copy()

#     def buscar_por_codigo(self, codigo):
#         codigo = codigo.strip() if isinstance(codigo, str) else ""

#         for producto in self._productos:
#             if producto.codigo == codigo:
#                 return producto

#         return None

#     def actualizar_existencias(self, codigo, nueva_cantidad):
#         producto = self.buscar_por_codigo(codigo)

#         if producto is None:
#             return False

#         return producto.actualizar_existencias(nueva_cantidad)

#     def eliminar_producto(self, codigo):
#         producto = self.buscar_por_codigo(codigo)

#         if producto is None:
#             return False

#         self._productos.remove(producto)
#         return True

#     def productos_sin_stock(self):
#         return [
#             producto
#             for producto in self._productos
#             if producto.cantidad == 0
#         ]

#     def resumen(self):
#         unidades = sum(
#             producto.cantidad for producto in self._productos
#         )

#         valor_total = sum(
#             producto.calcular_valor() for producto in self._productos
#         )

#         categorias = {
#             producto.categoria for producto in self._productos
#         }

#         return {
#             "productos_diferentes": len(self._productos),
#             "unidades_disponibles": unidades,
#             "valor_total": valor_total,
#             "categorias": categorias
#         }



class Inventario:
    def __init__(self):
        self._productos = []

    def registrar_producto(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def listar_productos(self):
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        if not isinstance(codigo, str):
            return None

        codigo = codigo.strip()

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        return producto.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        return [
            producto
            for producto in self._productos
            if producto.cantidad == 0
        ]

    def resumen(self):
        unidades = sum(
            producto.cantidad for producto in self._productos
        )

        valor_total = sum(
            producto.calcular_valor() for producto in self._productos
        )

        categorias = {
            producto.categoria for producto in self._productos
        }

        return {
            "productos_registrados": len(self._productos),
            "unidades_disponibles": unidades,
            "valor_total": valor_total,
            "categorias": categorias
        }

#NUEVO RETO 19

    def buscar_por_categoria(self, categoria):
        return [
            producto for producto in self._productos
            if producto.categoria == categoria
        ]

    def listar_ordenados_por_nombre(self):
        return sorted(
            self._productos,
            key=lambda producto: producto.nombre.lower()
        )


    def actualizar_precio(self, codigo, nuevo_precio):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        return producto.actualizar_precio(nuevo_precio)

        if (
            isinstance(nuevo_precio, bool)
            or not isinstance(nuevo_precio, (int, float))
            or nuevo_precio <= 0
        ):
            return False

        producto._precio = nuevo_precio
        return True

    def producto_mayor_valor(self):
        if not self._productos:
            return None

        return max(
            self._productos,
            key=lambda producto: producto.calcular_valor()
        )

    def diccionario_productos(self):
        return {
            producto.codigo: producto.nombre
            for producto in self._productos
        }