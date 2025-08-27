n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado com média", media)
elif media >= 5:
    print("Recuperação com média", media)
else:
    print("Reprovado com média", media)