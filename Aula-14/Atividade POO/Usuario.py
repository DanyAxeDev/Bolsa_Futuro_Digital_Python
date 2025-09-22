class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha

    def __str__(self):
        return f"Usuário: {self.nome}\nE-mail: {self.email}"
    
    def verificarSenha(self, senha):
        if senha == self.__senha:
            return True
        else:
            return False