import random

def numeroSecreto():
    numeroSecreto = random.randint(1, 100)

    numeroUsuario = int(input("\nDigite um número entre 1 e 100 (maximo 5 tentativas): "))
    qtd = 0

    while numeroUsuario != numeroSecreto:
        qtd += 1
        if numeroUsuario < numeroSecreto:
            print("O número secreto é maior.")
        elif numeroUsuario > numeroSecreto:
            print("O número secreto é menor.")
        if qtd >= 5:
            print("\nVocê atingiu o limite de tentativas. O número secreto era:", numeroSecreto)
            break

        numeroUsuario = int(input("\nTentativa nº {}: ".format(qtd + 1)))

    if qtd + 1 <= 5:
        print(f"\nParabéns! Você acertou o número secreto em {qtd + 1} tentativas. O número era {numeroSecreto}.")

replay = True

while replay:
    numeroSecreto()
    resposta = input("Deseja jogar novamente? (s/n):").strip().lower()
    if resposta != 's':
        replay = False
        print("\nObrigado por jogar!")