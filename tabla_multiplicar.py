numero = int(input("Número: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)

#PS C:\Users\PC\Desktop\python-laboratorio2> python tabla_multiplicar.py
#Número: 7 
#7 x 1 = 7  
#7 x 2 = 14 
#7 x 3 = 21 
#7 x 4 = 28 
#7 x 5 = 35 
#7 x 6 = 42 
#7 x 7 = 49 
#7 x 8 = 56 
#7 x 9 = 63 
#7 x 10 = 70