numero = int(input("Digite um número (digite 0 para sair): "))

while numero != 0:
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

    numero = int(input("Digite outro número (digite 0 para sair): "))

print("Programa encerrado.")