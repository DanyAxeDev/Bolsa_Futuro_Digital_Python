from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome, email, senha, endereco, conta):
        super().__init__(nome, email, senha)
        self.endereco = endereco
        self.conta = conta

    def __str__(self):
        return super().__str__() + f"\nEndereço: {self.endereco}"
    
