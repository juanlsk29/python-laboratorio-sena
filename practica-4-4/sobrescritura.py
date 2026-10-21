class Notificacion:
    def enviar(self):
        return "Enviando notificación general"


class Correo(Notificacion):
    def enviar(self):
        return "Enviando correo electrónico"


class MensajeTexto(Notificacion):
    def enviar(self):
        return "Enviando mensaje de texto"


notificaciones = [Notificacion(), Correo(), MensajeTexto()]

for notificacion in notificaciones:
    print(notificacion.enviar())

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-4> python sobrescritura.py 
# Enviando notificación general
# Enviando correo electrónico
# Enviando mensaje de texto