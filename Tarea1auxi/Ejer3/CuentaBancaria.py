class CuentaBancaria:
    def __init__(self, titular, nroCuenta, saldo):
        self.titular = titular
        self.nroCuenta = nroCuenta
        self.saldo = saldo
    def depositar(self, monto):
        if monto <= 0:
            print("ERROR: No se puede depositar un numero negativo o 0.")
            return
        self.saldo = self.saldo + monto
        print("Deposito exitoso. Nuevo saldo:", self.saldo)
    def retirar(self, monto):
        if monto > self.saldo:
            print("ERROR: Saldo insuficiente. Saldo actual:", self.saldo)
            return
        self.saldo = self.saldo - monto
        print("Retiro exitoso. Nuevo saldo:", self.saldo)
    def mostrar(self):
        print("Titular:", self.titular)
        print("Nro. Cuenta:", self.nroCuenta)
        print("Saldo:", self.saldo)