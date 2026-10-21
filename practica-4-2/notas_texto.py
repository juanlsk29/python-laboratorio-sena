with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera observación\n")
    archivo.write("Segunda observación\n")

with open("notas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-2> python notas_texto.py
# Primera observación
# Segunda observación