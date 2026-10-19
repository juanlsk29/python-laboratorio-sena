class Billetera:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def registrar_ingreso(self, monto):
        if monto <= 0:
            print("Error: el ingreso debe ser positivo.")
            return

        self.saldo += monto
        print("Ingreso registrado:", monto)

    def registrar_gasto(self, monto):
        if monto <= 0:
            print("Error: el gasto debe ser positivo.")
            return

        if monto > self.saldo:
            print("Error: saldo insuficiente.")
            return

        self.saldo -= monto
        print("Gasto registrado:", monto)

    def consultar_saldo(self):
        return self.saldo


billetera1 = Billetera("Juan")
billetera2 = Billetera("Anthony")

billetera1.registrar_ingreso(100000)
billetera1.registrar_gasto(30000)

billetera2.registrar_ingreso(50000)
billetera2.registrar_gasto(10000)

billetera1.registrar_gasto(100000)
billetera2.registrar_ingreso(-5000)

print("Saldo de Juan:", billetera1.consultar_saldo())
print("Saldo de Anthony:", billetera2.consultar_saldo())

# RESULTADO   
# PS C:\Users\PC\Desktop\python-laboratorio3> cd practica-3-3    
# PS C:\Users\PC\Desktop\python-laboratorio3\practica-3-3> python billetera.py
# Ingreso registrado: 100000
# Gasto registrado: 30000
# Ingreso registrado: 50000
# Gasto registrado: 10000
# Error: saldo insuficiente.
# Error: el ingreso debe ser positivo.
# Saldo de Juan: 70000
# Saldo de Anthony: 40000