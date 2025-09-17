class Midia():
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    def exibirInfo(self):
        return f"*****************\nTitulo: {self.titulo}\nAno: {self.ano}"
    
class Filme(Midia):
    def __init__(self, titulo, ano, diretor, duracao):
        super().__init__(titulo, ano)
        self.diretor = diretor
        self.duracao = duracao

    def exibirInfo(self):
        return super().exibirInfo() + f"\nDiretor: {self.diretor}\nDuracao: {self.duracao} min"
    
class Livro(Midia):
    def __init__(self, titulo, ano, autor, paginas):
        super().__init__(titulo, ano)
        self.autor = autor
        self.paginas = paginas

    def exibirInfo(self):
        return super().exibirInfo() + f"\nAutor: {self.autor}\nPáginas: {self.paginas}"
    
if __name__ == "__main__":
    filme = Filme("Kung fu panda", 2008, "Mark Osborne", 92)
    livro = Livro("Harry Potter", 1998, "J. K. Rowling", 332)

    midias = [filme, livro]

    for midia in midias:
        print(midia.exibirInfo())