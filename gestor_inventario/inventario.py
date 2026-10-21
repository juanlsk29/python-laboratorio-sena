from producto import Producto


class Inventario:
    def __init__(self):
        self._productos = []

    def registrar(self, producto):
        if not isinstance(producto, Producto):
            raise ValueError("Debe registrar un objeto Producto.")

        if self.buscar(producto.codigo) is not None:
            raise ValueError("Ya existe un producto con ese código.")

        self._productos.append(producto)

    def listar(self):
        return self._productos.copy()

    def buscar(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_existencias(self, codigo, cantidad):
        producto = self.buscar(codigo)

        if producto is None:
            raise ValueError("No existe un producto con ese código.")

        producto.actualizar_cantidad(cantidad)

    def eliminar(self, codigo):
        producto = self.buscar(codigo)

        if producto is None:
            raise ValueError("No existe un producto con ese código.")

        self._productos.remove(producto)

    def productos_sin_stock(self):
        return [
            producto
            for producto in self._productos
            if producto.cantidad == 0
        ]

    def resumen(self):
        total_productos = len(self._productos)
        unidades = sum(p.cantidad for p in self._productos)
        valor = sum(
            p.precio * p.cantidad for p in self._productos
        )

        return {
            "productos": total_productos,
            "unidades": unidades,
            "valor_total": valor
        }

    def exportar_datos(self):
        return [
            producto.a_diccionario()
            for producto in self._productos
        ]

    def cargar_datos(self, registros):
        temporal = Inventario()

        for registro in registros:
            producto = Producto.desde_diccionario(registro)
            temporal.registrar(producto)

        self._productos = temporal._productos.copy()
