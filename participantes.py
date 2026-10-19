grupo_a = ["Ana", "Carlos", "Laura", "Ana"]
grupo_b = ["Laura", "David", "Carlos", "Pablo", "David"]

participantes = set(grupo_a + grupo_b)

print("Participantes únicos:", participantes)
print("Cantidad de personas:", len(participantes))

participantes.add("Santiago")
print("Después de agregar a Santiago:", participantes)

participantes.discard("Ana")
print("Después de eliminar a Ana:", participantes)

print("Cantidad final:", len(participantes))

#PS C:\Users\PC\Desktop\python-laboratorio2> python participantes.py
#Participantes únicos: {'Pablo', 'Ana', 'Carlos', 'Laura', 'David'}
#Cantidad de personas: 5
#Después de agregar a Santiago: {'Pablo', 'Ana', 'Santiago', 'Carlos', 'Laura', 'David'}
#Después de eliminar a Ana: {'Pablo', 'Santiago', 'Carlos', 'Laura', 'David'}
#Cantidad final: 5