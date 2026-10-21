with open("pruebas.txt", "r", encoding="utf-8") as archivo:
    for numero, linea in enumerate(archivo, start=1):
        print(numero, "-", linea.strip())

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python bitacora.py
# Nombre de la prueba: Prueba dos de Python 
# Resultado (aprobada/fallida): fallida
# Observación breve: Prueba para recorrer_lineas
# Prueba guardada correctamente.

# RESULTADO 
# Prueba: Prueba Python | Resultado: aprobada | Observación: Mi primera bitacora 
# Prueba: Prueba dos de Python  | Resultado: fallida | Observación: Prueba para recorrer_lineas
