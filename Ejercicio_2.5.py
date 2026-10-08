class CuentaBancaria:

    def __init__(self, nombres, apellidos, numero, tipo, interes):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero = numero
        self.tipo = tipo
        self.saldo = 0
        self.interes = interes

    def mostrar(self):
        print("Nombre:", self.nombres)
        print("Apellidos:", self.apellidos)
        print("Número:", self.numero)
        print("Tipo:", self.tipo)
        print("Saldo:", self.saldo)
        print("Interés mensual:", self.interes, "%")

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, valor):
        self.saldo += valor

    def retirar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes / 100


cuenta = CuentaBancaria(
    "Samuel",
    "Arango",
    "123456",
    "Ahorros",
    2
)

cuenta.mostrar()

cuenta.consignar(100000)
print("Saldo:", cuenta.consultar_saldo())

cuenta.retirar(30000)
print("Saldo:", cuenta.consultar_saldo())

cuenta.aplicar_interes()
print("Saldo con interés:", cuenta.consultar_saldo())