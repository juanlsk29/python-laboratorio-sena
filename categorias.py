categorias = ("Perifericos", "Componentes", "Accesorios")

for categoria in categorias:
    print(categoria)

elegida = input("Categoría: ").strip()

if elegida in categorias:
    print("Categoría válida.")
else:
    print("Categoría no registrada.")

#PS C:\Users\PC\Desktop\python-laboratorio2> python categorias.py
#Perifericos
#Componentes
#Accesorios
#Categoría: Perifericos
#Categoría válida.