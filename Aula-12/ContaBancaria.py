class ContaBancaria():
    def __init__(self, saldoInicial = 0):
        self.__saldo = saldoInicial

    def depositar(self, valor):
        if(valor < 0):
            print("Insira um valor válido para depósito")
        else:
            self.__saldo += valor
    
    def sacar(self, valor):
        if(valor <= 0):
            print("Valor inválido para saque")
        elif(valor > self.__saldo):
            print("Valor para saque é maior que o valor na conta")
        else:
            self.__saldo -= valor
    
    def consultarSaldo(self):
        return self.__saldo
    
if __name__ == "__main__":
    c = ContaBancaria()

    c.depositar(1000)

    c.sacar(2000)

    c.sacar(-100)

    c.sacar(300)

    print(c.consultarSaldo())