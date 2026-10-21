# V1
# CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


# class Producto:
#     def __init__(self, codigo, nombre, categoria, precio, cantidad):
#         codigo = codigo.strip() if isinstance(codigo, str) else ""
#         nombre = nombre.strip() if isinstance(nombre, str) else ""

#         if not codigo:
#             raise ValueError("El código no puede estar vacío.")

#         if not nombre:
#             raise ValueError("El nombre no puede estar vacío.")

#         if categoria not in CATEGORIAS:
#             raise ValueError("La categoría seleccionada no está permitida.")

#         if isinstance(precio, bool) or not isinstance(precio, (int, float)):
#             raise ValueError("El precio debe ser numérico.")

#         if precio <= 0:
#             raise ValueError("El precio debe ser mayor que cero.")

#         if isinstance(cantidad, bool) or not isinstance(cantidad, int):
#             raise ValueError("La cantidad debe ser un número entero.")

#         if cantidad < 0:
#             raise ValueError("La cantidad no puede ser negativa.")

#         self._codigo = codigo
#         self._nombre = nombre
#         self._categoria = categoria
#         self._precio = precio
#         self._cantidad = cantidad

#     @property
#     def codigo(self):
#         return self._codigo

#     @property
#     def nombre(self):
#         return self._nombre

#     @property
#     def categoria(self):
#         return self._categoria

#     @property
#     def precio(self):
#         return self._precio

#     @property
#     def cantidad(self):
#         return self._cantidad

#     def actualizar_existencias(self, nueva_cantidad):
#         if isinstance(nueva_cantidad, bool) or not isinstance(
#             nueva_cantidad, int
#         ):
#             return False

#         if nueva_cantidad < 0:
#             return False

#         self._cantidad = nueva_cantidad
#         return True

#     def calcular_valor(self):
#         return self._precio * self._cantidad


CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if categoria not in CATEGORIAS:
            raise ValueError("La categoría no está permitida.")

        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser numérico.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un entero.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if isinstance(nueva_cantidad, bool) or not isinstance(
            nueva_cantidad, int
        ):
            return False

        if nueva_cantidad < 0:
            return False

        self._cantidad = nueva_cantidad
        return True

    def calcular_valor(self):
        return self._precio * self._cantidad

#NUEVO RETO 19


    def actualizar_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, bool):
            return False

        if not isinstance(nuevo_precio, (int, float)):
            return False

        if nuevo_precio <= 0:
            return False

        self._precio = nuevo_precio
        return True
