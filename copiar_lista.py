original = ["Teclado", "Mouse"]
otra_referencia = original

otra_referencia.append("Monitor")

print("Primera prueba:")
print("Original:", original)
print("Otra referencia:", otra_referencia)

original = ["Teclado", "Mouse"]
copia = original.copy()

copia.append("Monitor")

print()
print("Segunda prueba:")
print("Original:", original)
print("Copia:", copia)

#PS C:\Users\PC\Desktop\python-laboratorio2> python copiar_lista.py
#Primera prueba:
#Original: ['Teclado', 'Mouse', 'Monitor']       
#Otra referencia: ['Teclado', 'Mouse', 'Monitor']

#Segunda prueba:
#Original: ['Teclado', 'Mouse']
#Copia: ['Teclado', 'Mouse', 'Monitor']