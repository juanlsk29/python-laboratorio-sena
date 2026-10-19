codigos = [" p001 ", "P002", "", " p003", "  "]

codigos_normalizados = [
    codigo.strip().upper()
    for codigo in codigos
    if codigo.strip() != ""
]

print(codigos_normalizados)

#PS C:\Users\PC\Desktop\python-laboratorio2> python normalizar_codigos.py
#['P001', 'P002', 'P003']