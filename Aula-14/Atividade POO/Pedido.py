from ItemPedido import ItemPedido

class Pedido():
    def __init__(self, cliente, vendedor, itens=[]):
        self.cliente = cliente
        self.vendedor = vendedor
        self.itens = []
        for item in itens:
            p = ItemPedido(item.produto, item.qtd)
            self.itens.append(p)

    def adicionarItem(self, produto, qtd):
        if(produto.temEstoque()):
            p = ItemPedido(produto, qtd)
            self.itens.append(p)

    def total(self):
        total = 0
        for item in self.itens:
            total += item.subTotal()

        return total
    
    def fecharPedido(self):
        senha = input("Confirme sua senha de usuário: ")

        if(self.cliente.verificarSenha(senha)):
            print("\nFechando pedido....")
            self.cliente.conta.sacar(self.total())
            self.vendedor.conta.depositar(self.total())
            for item in self.itens:
                item.produto.atualizarEstoque(item.produto.getEstoque() - item.qtd)
        else:
            print("Senhas não batem, não foi possível fechar o pedido")

    def __str__(self):
        i = ""
        for item in self.itens:
            i += f"{item.qtd} {item.produto.nome}..........{item.produto.preco}\nSubtotal: R${item.subTotal()}\n" 
        return f"***** Pedido de {self.cliente.nome} *****\n" + i + f"\tTotal: R${self.total()}" + f"\n\n***** {self.vendedor.loja} *****"