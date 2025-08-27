nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if(media >= 6):
    print("Aluno foi aprovado com média", media)
elif(media >=5 and media < 6):
    print("Aluno de recuperação com média", media)
else:
    print("Aluno foi reprovado com média", media)