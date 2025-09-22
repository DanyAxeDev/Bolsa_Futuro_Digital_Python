class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque

    def __str__(self):
        return f"***** {self.nome} *****\nPreço: R${self.preco}\nEstoque: {self.estoque}"
    
    def __eq__(self, other):
        if isinstance(other, Produto):
            return self.nome == other.nome and self.preco == other.preco
        return False
    
    def atualizarEstoque(self, valor):
        self.__estoque = valor
    
    def getEstoque(self):
        return self.__estoque

    def temEstoque(self):
        return self.__estoque > 0