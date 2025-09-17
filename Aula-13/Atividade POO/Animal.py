class Animal():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def emitirSom(self):
        return f"Som genérico de animal"
    
    def comer(self):
        return f"O animal está comendo"
    
    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade
    
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca

    def emitirSom(self):
        return f"Au Au"
    
    def correr(self):
        return f"O cachorro {self.__nome} da raça {self.__raca} está correndo"
    
    def getRaca(self):
        return self.__raca
    
    def setRaca(self, raca):
        self.__raca = raca
    
class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.__cor = cor

    def emitirSom(self):
        return "Miau"
    
    def subirEmArvore(self):
        return f"O gato {self.__nome} da cor {self.__cor} está subindo na arvore"
    
    def getCor(self):
        return self.__cor
    
    def setCor(self, cor):
        self.__cor = cor
    
class Passaro(Animal):
    def __init__(self, nome, idade, tipo):
        super().__init__(nome, idade)
        self.__tipo = tipo

    def emitirSom(self):
        return "Piu Piu"
    
    def voar(self):
        return f"O pássaro {self.__nome} do tipo {self.__tipo} está voando"
    
    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo

