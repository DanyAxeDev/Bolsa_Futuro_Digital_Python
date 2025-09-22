from Usuario import Usuario

class Vendedor(Usuario):
    def __init__(self, nome, email, senha, loja, conta):
        super().__init__(nome, email, senha)
        self.loja = loja
        self.conta = conta

    def __str__(self):
        return super().__str__() + f"\nLoja: {self.loja}"