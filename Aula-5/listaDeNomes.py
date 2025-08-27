nomes = {}

parar = False

while not parar:
    nome = input("Digite um nome (ou 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        parar = True
    else:
        if nome[0].upper() not in nomes:
            nomes[nome[0].upper()] = {nome}
        else:
            nomes[nome[0].upper()].add(nome)

nomes = dict(sorted(nomes.items()))

print("Nomes na lista:")
for letra, nome in nomes.items():
    print("Nomes com a letra", letra)
    for n in nome:
        print(" - ", n)