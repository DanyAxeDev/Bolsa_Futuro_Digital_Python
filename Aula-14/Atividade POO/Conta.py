class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def sacar(self, valor):
        if(valor < 0):
            print("Saque um valor válido")
        elif(valor > self.__saldo):
            print("Valor para saque maior que o valor da conta")
        else:
            self.__saldo -= valor

    def depositar(self, valor):
        if(valor < 0):
            print("Valor inválido para deposito")
        else:
            self.__saldo += valor

    def getSaldo(self):
        return f"R${self.__saldo}"