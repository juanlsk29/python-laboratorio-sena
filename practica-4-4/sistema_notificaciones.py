class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError(
            "Las clases especializadas deben implementar enviar()."
        )


class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando correo electrónico: {mensaje}")


class NotificacionConsola(Notificacion):
    def enviar(self, mensaje):
        print(f"Notificación en consola: {mensaje}")


notificaciones = [
    NotificacionCorreo(),
    NotificacionConsola()
]

mensaje = "El inventario se ha actualizado."

for notificacion in notificaciones:
    notificacion.enviar(mensaje)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-4> python sistema_notificaciones.py
# Enviando correo electrónico: El inventario se ha actualizado.
# Notificación en consola: El inventario se ha actualizado.