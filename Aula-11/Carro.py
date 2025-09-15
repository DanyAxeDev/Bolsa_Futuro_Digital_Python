class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_dados(self):
        print(f"Carro da marca {self.marca}, modelo {self.modelo} {self.ano}")

meuCarro = Carro("Toyota", "Corolla", 2020)

meuCarro.exibir_dados()