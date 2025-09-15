class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
    
    def __str__(self):
        return f"\n******* {self.__nome.upper()} *******\nPreço: R${self.__preco}\nEstoque: {self.__estoque}"
    
    def getNome(self):
        return self.__nome
    
    def getPreco(self):
        return self.__preco
    
    def getEstoque(self):
        return self.__estoque
    
    def aplicarDesconto(self, percentual):
        self.__preco *= (100 - percentual)/100
    
if __name__ == "__main__":
    p1 = Produto("Notebook", 3500, 10)
    print(p1)

    p1.aplicarDesconto(90)
    print(p1)