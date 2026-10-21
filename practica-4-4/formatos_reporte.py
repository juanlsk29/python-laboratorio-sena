class ReporteTexto:
    def generar(self, datos):
        return f"Registros del reporte: {datos}"


class ReporteResumen:
    def generar(self, datos):
        return f"Cantidad de registros: {len(datos)}"


datos = ["Teclado", "Mouse", "Monitor"]

reportes = [ReporteTexto(), ReporteResumen()]

for reporte in reportes:
    print(reporte.generar(datos))

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-4> python formatos_reporte.py
# Registros del reporte: ['Teclado', 'Mouse', 'Monitor']
# Cantidad de registros: 3