from Produto import Produto
from Cliente import Cliente
from Pedido import Pedido
from Vendedor import Vendedor
from Conta import Conta

p1 = Produto("Notebook", 3500.0, 10)
p2 = Produto("Mouse", 150.0, 50)

contaCliente = Conta(10000)
cliente1 = Cliente("Ana", "ana@email.com", "123456", "Rua A, 123", contaCliente)
contaVendedor = Conta(20000)
vendedor1 = Vendedor("Daniel", "daniel@gmail.com", "654321", "Daniels Eletronics", contaVendedor)

pedido = Pedido(cliente1, vendedor1)
pedido.adicionarItem(p1, 1)
pedido.adicionarItem(p2, 2)

print(f"Conta da {cliente1.nome} antes do pedido: {cliente1.conta.getSaldo()}")
print(f"Conta do {vendedor1.nome} antes do pedido {vendedor1.conta.getSaldo()}")
print(f"Estoque do {p1.nome}: {p1.getEstoque()}")
print(f"Estoque do {p2.nome}: {p2.getEstoque()}")

print(pedido)

pedido.fecharPedido()

print(f"Conta da {cliente1.nome} depois do pedido: {cliente1.conta.getSaldo()}")
print(f"Conta do {vendedor1.nome} depois do pedido {vendedor1.conta.getSaldo()}")
print(f"Estoque do {p1.nome}: {p1.getEstoque()}")
print(f"Estoque do {p2.nome}: {p2.getEstoque()}")