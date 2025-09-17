class Animal():
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie
    
    def emitirSom(self):
        return f"Som genérico de animal"
    
    def info(self):
        return f"{self.nome}, {self.idade} anos, {self.especie}"
    
class Mamifero(Animal):
    def __init__(self, nome, idade, especie, pelagem):
        super().__init__(nome, idade, especie)
        self.pelagem = pelagem

    def emitirSom(self):
        return "Som de mamífero"
    
    def info(self):
        return super().info() + f", pelagem {self.pelagem}"
    
class Ave(Animal):
    def __init__(self, nome, idade, especie, voa = True):
        super().__init__(nome, idade, especie)
        self.voa = voa

    def emitirSom(self):
        return f"Som de ave"
    
    def info(self):
        return super().info() + f", é voadora" if self.voa else super().info() + f", não é voadora"
    
class Reptil(Animal):
    def __init__(self, nome, idade, especie, alimentacao):
        super().__init__(nome, idade, especie)
        self.alimentacao = alimentacao

    def emitirSom(self):
        return "Som de réptil"
    
    def info(self):
        return super().info() + f", alimentação baseada em {self.alimentacao}"
    
if __name__ == "__main__":
    mam = Mamifero("Alex", 5, "Leão", "amarela")
    ave = Ave("louro", 12, "Papagaio", False)
    rep = Reptil("verno", 100, "Tartaruga", "insetos")

    animais = [mam, ave, rep]

    for animal in animais:
        print(animal.emitirSom())
        print(animal.info())