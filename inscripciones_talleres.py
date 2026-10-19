python = {"Ana", "Carlos", "Laura", "Santiago", "María"}
java = {"Laura", "Santiago", "David", "Pablo"}

print("Inscritos en al menos un taller:", python | java)
print("Inscritos en ambos talleres:", python & java)
print("Únicamente en Python:", python - java)
print("Únicamente en Java:", java - python)
print("Inscritos en un solo taller:", python ^ java)

#PS C:\Users\PC\Desktop\python-laboratorio2> python inscripciones_talleres.py
#Inscritos en al menos un taller: {'Pablo', 'María', 'David', 'Santiago', 'Ana', 'Laura', 'Carlos'}
#Inscritos en ambos talleres: {'Laura', 'Santiago'}
#Únicamente en Python: {'Ana', 'María', 'Carlos'}
#Únicamente en Java: {'David', 'Pablo'}
#Inscritos en un solo taller: {'Pablo', 'María', 'David', 'Ana', 'Carlos'}