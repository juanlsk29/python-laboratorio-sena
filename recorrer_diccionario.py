producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0
}

print("Claves:")

for clave in producto:
    print(clave)

print("\nValores:")

for valor in producto.values():
    print(valor)

print("\nClaves y valores:")

for clave, valor in producto.items():
    print(clave, ":", valor)

#PS C:\Users\PC\Desktop\python-laboratorio2> python recorrer_diccionario.py
#Claves:
#codigo  
#nombre  
#precio  
        
#Valores:
#P001    
#Teclado 
#85000.0 

#Claves y valores:
#codigo : P001
#nombre : Teclado
#precio : 85000.0