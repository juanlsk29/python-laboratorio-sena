nombre = input("Nombre de la prueba: ")
resultado = input("Resultado (aprobada/fallida): ").strip().lower()
observacion = input("Observación breve: ")

if resultado not in ("aprobada", "fallida"):
    print("Resultado inválido. Debes escribir aprobada o fallida.")
else:
    with open("pruebas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(
            f"Prueba: {nombre} | Resultado: {resultado} | "
            f"Observación: {observacion}\n"
        )

    print("Prueba guardada correctamente.")

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python bitacora.py
# Nombre de la prueba: Prueba Python
# Resultado (aprobada/fallida): aprobada
# Observación breve: Mi primera bitacora 
# Prueba guardada correctamente.

# RESULTADO
# Prueba: Prueba Python | Resultado: aprobada | Observación: Mi primera bitacora 
