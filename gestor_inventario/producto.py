import math


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

        if not math.isfinite(precio) or precio <= 0:
            raise ValueError("El precio debe ser positivo y finito.")

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad < 0
        ):
            raise ValueError(
                "La cantidad debe ser un entero no negativo."
            )

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = float(precio)
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

    def actualizar_cantidad(self, nueva_cantidad):
        if (
            isinstance(nueva_cantidad, bool)
            or not isinstance(nueva_cantidad, int)
            or nueva_cantidad < 0
        ):
            raise ValueError(
                "La cantidad debe ser un entero no negativo."
            )

        self._cantidad = nueva_cantidad

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos):
        campos = {
            "codigo", "nombre", "categoria", "precio", "cantidad"
        }

        if not isinstance(datos, dict) or not campos.issubset(datos):
            raise ValueError("El registro del producto está incompleto.")

        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
        )

    def __str__(self):
        return (
            f"{self.codigo} | {self.nombre} | {self.categoria} | "
            f"${self.precio:.2f} | Cantidad: {self.cantidad}"
        )

def exportar_datos(self):
    return [producto.a_diccionario() for producto in self._productos]