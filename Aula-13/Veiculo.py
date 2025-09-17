class Veiculo():
    def __init__(self, marca, velocidade):
        self.marca = marca
        self.velocidade = velocidade
    
    def mover(self):
        return f"Veiculo {self.marca} se movendo"
    
class Carro(Veiculo):
    def __init__(self, marca, velocidade, ligado = False):
        super().__init__(marca, velocidade)
        self.ligado = ligado

    def ligarMotor(self):
        if(self.ligado):
            return f"Carro {self.marca} já está ligado"
        else:
            self.ligado = True
            return f"Carro {self.marca} ligando..."
    
    def mover(self):
        if(self.ligado):
            return f"Carro {self.marca} acelerando até {self.velocidade} Km/h"
        else:
            return f"Ligue o carro primeiro"
    
class Bicicleta(Veiculo):
    def __init__(self, marca, velocidade):
        super().__init__(marca, velocidade)

    def mover(self):
        return f"Bicicleta {self.marca} pedalando até {self.velocidade} Km/h"

    def pedalar(self):
        return f"Pedalando a bicicleta {self.marca}"
    
if __name__ == '__main__':
    veiculos = [Carro("Toyota", 120, True), Bicicleta("Caloi", 25)]

    for v in veiculos:
        print(v.mover())