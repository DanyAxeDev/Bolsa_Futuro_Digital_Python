class Livro:
    # Função que é executada quando um objeto é instanciado a partir dessa classe
    # Define nossos atributos
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = True

    # Função para exibir os dados do nosso livro
    def exibirInfo(self):
        '''Função para exibir todos os dados do livro
        '''
        print("\n",20*"*")
        print(f"Nome: {self.titulo}\nAutor(a): {self.autor}\nAno: {self.ano}\nStatus: {"Disponivel" if self.status else "Emprestado"}\n")
    
    def emprestar(self):
        self.status = False

    def devolver(self):
        self.status = True