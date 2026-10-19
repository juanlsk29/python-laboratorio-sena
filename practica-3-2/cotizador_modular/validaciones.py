def precio_valido(precio):
    return precio > 0


def cantidad_valida(cantidad):
    return cantidad > 0 and cantidad.is_integer()


def porcentaje_valido(porcentaje):
    return 0 <= porcentaje <= 100
