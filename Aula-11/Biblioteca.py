from Livro import Livro

class Bibliteca:
    def __init__(self):
        self.livros = []

    def adicionarLivro(self):
        titulo = input("Digite o nome do livro que deseja adicionar: ")
        autor = input("Digite o(a) autor(a): ")
        ano = int(input("Digite o ano de publicaçao: "))

        livro = Livro(titulo, autor, ano)
        self.livros.append(livro)
    
    def listarLivros(self):
        for livro in self.livros:
            livro.exibirInfo()

    def emprestarLivro(self):
        titulo = input("Digite o nome do livro que deseja emprestar: ")
        for livro in self.livros:
            if livro.titulo == titulo:
                if(livro.status == False):
                    print("Livro já foi emprestado")
                    break
                else:
                    livro.emprestar()
                    break
            print("\nLivro não encontrado")
    
    def devolverLivro(self):
        titulo = input("Digite o nome do livro que deseja devolver: ")
        for livro in self.livros:
            if livro.titulo == titulo:
                if(livro.status == True):
                    print("Livro já foi devolvido")
                    break
                else:
                    livro.devolver()
                    break
            print("\nLivro não encontrado")

    def exibirMenu(self):
        print("\n","*"*10, " SISTEMA DE BIBLIOTECA ", "*"*10)
        print("1 - Adicionar livro")
        print("2 - Listar livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("5 - Sair")

if __name__ == "__main__":
    biblioteca = Bibliteca()

    continuar = 0

    while continuar != '5':
        biblioteca.exibirMenu()

        continuar = input("Digite sua opção: ")

        match continuar:
            case '1':
                biblioteca.adicionarLivro()
            case '2':
                biblioteca.listarLivros()
            case '3':
                biblioteca.emprestarLivro()
            case '4':
                biblioteca.devolverLivro()
            case '5':
                print("Saindo da biblioteca")
            case _:
                print("\nDigite um valor válido")
