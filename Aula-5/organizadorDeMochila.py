mochila = ["camiseta", "calça", "meias", "escova", "carregador", "livro"]

mochila.remove("livro")
mochila.pop(2)

mochila.append("remedios")

mochila[0] = "jaqueta"

mochilaOrdenada = sorted(mochila)

print("mochila final: ")
for item in mochilaOrdenada:
    print(item)
