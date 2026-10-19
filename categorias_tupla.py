categorias = ("Periféricos", "Accesorios", "Componentes", "Papelería")

print("Categorías disponibles:")

for numero, categoria in enumerate(categorias, start=1):
    print(f"{numero}. {categoria}")

busqueda = input("\nEscribe una categoría: ").strip()

if busqueda in categorias:
    print("La categoría está permitida.")
else:
    print("La categoría no está permitida.")

print("Cantidad de categorías disponibles:", len(categorias))

#PS C:\Users\PC\Desktop\python-laboratorio2> python categorias_tupla.py
#Categorías disponibles:
#1. Periféricos
#2. Accesorios
#3. Componentes
#4. Papelería

#Escribe una categoría: Accesorios
#La categoría está permitida.
#Cantidad de categorías disponibles: 4