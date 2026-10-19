grupo_a = {"Ana", "Carlos", "Laura", "Sara"}
grupo_b = {"Laura", "Sara", "David", "Pablo"}

print("Unión:", grupo_a | grupo_b)
print("Intersección:", grupo_a & grupo_b)
print("Solo A:", grupo_a - grupo_b)
print("Diferencia simétrica:", grupo_a ^ grupo_b)

#PS C:\Users\PC\Desktop\python-laboratorio2> python operaciones_conjuntos.py
#Unión: {'Sara', 'David', 'Laura', 'Carlos', 'Pablo', 'Ana'}
#Intersección: {'Laura', 'Sara'}
#Solo A: {'Carlos', 'Ana'}
#Diferencia simétrica: {'David', 'Carlos', 'Pablo', 'Ana'}