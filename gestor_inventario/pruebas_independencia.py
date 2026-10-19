
from inventario import Inventario
from producto import Producto

primero = Inventario()
segundo = Inventario()

primero.registrar_producto(
    Producto("P001", "Teclado", "Periféricos", 85000, 4)
)

print("Primero:", len(primero.listar_productos()))
print("Segundo:", len(segundo.listar_productos()))

# PS C:\Users\PC\Desktop\python-laboratorio3\gestor_inventario> python pruebas_independencia.py
# Primero: 1
# Segundo: 0