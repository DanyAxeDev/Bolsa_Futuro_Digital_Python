nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
curso = input("Diga o curso que você faz: ")
nota1 = float(input("Diga a sua primeira nota: "))
nota2 = float(input("Diga a sua segunda nota: "))

media = (nota1 + nota2)/2
resultado = ""

if(media >= 6):
    resultado = "foi aprovado"
elif(media >=5 and media < 6):
    resultado = "está de recuperação"
else:
    resultado = "foi reprovado"

print("Olá", nome, ", você", resultado, "no curso", curso,"com média", media)