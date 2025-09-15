class Cliente:
    def __init__(self, nome, email, cpf, saldoPrincipal = 0):
        self.nome = nome
        self.email = email
        self.__cpf = cpf
        self.__saldo = saldoPrincipal

    def getCpf(self):
        return self.__cpf
    
    def getSaldo(self):
        return self.__saldo
    
    def adicionarSaldo(self, valor):
        if(valor < 0):
            print("Valor adicionado deve ser maior que zero")
        else:
            self.__saldo += valor

    def exibirDados(self):
        return f"Cliente: {self.nome}\nEmail: {self.email}"
    
if __name__ == "__main__":
    c = Cliente("Daniel", "danielmac789@gmail.com", "708.358.131-26", 500)

    print(c.nome)
    print(c.email)
    print(c.getCpf())
    print(c.getSaldo())

    c.adicionarSaldo(1000)

    print(c.getSaldo())