class ItemPedido():
    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd

    def subTotal(self):
        return self.produto.preco * self.qtd