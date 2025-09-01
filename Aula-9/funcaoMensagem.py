def message(**kwargs):
    for nome, curso in kwargs.items():
        print(f"Olá {nome}, bem vindo ao curso de {curso}")

if __name__ == '__main__':
    nome = input("Digite um nome: ")
    curso = input("Digite o nome do curso: ")

    message(daniel="python")