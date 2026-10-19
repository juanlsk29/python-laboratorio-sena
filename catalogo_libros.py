libros = [
    {
        "codigo": "L001",
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "anio": 1967
    },
    {
        "codigo": "L002",
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "anio": 1943
    },
    {
        "codigo": "L003",
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "anio": 1605
    }
]

codigo_buscado = input("Ingresa el código del libro que deseas buscar: ").strip()
encontrado = False

for libro in libros:
    if libro["codigo"] == codigo_buscado:
        print("\nLibro encontrado:")
        for clave, valor in libro.items():
            print(clave, ":", valor)
        encontrado = True
        break

if not encontrado:
    print("El libro no fue localizado.")

respuesta = input("\n¿Deseas registrar un nuevo libro? (si/no): ").strip().lower()

if respuesta == "si":
    nuevo_codigo = input("Código: ").strip()

    codigo_repetido = False

    for libro in libros:
        if libro["codigo"] == nuevo_codigo:
            codigo_repetido = True
            break

    if codigo_repetido:
        print("Error: ya existe un libro con ese código.")
    else:
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        anio = int(input("Año de publicación: "))

        nuevo_libro = {
            "codigo": nuevo_codigo,
            "titulo": titulo,
            "autor": autor,
            "anio": anio
        }

        libros.append(nuevo_libro)
        print("Libro registrado correctamente.")

print("\nCatálogo de libros:")

for libro in libros:
    print(libro["codigo"], "-", libro["titulo"])

