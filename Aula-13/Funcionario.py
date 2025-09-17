class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibirDados(self):
        return f"******************\nNome: {self.nome}\nSalário: R${self.salario}"
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibirDados(self):
        return super().exibirDados() + f"\nDepartamento: {self.departamento}"

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibirDados(self):
        return super().exibirDados() + f"\nLinguagem: {self.linguagem}"
    
if __name__ == '__main__':
    func = Funcionario("Ana", 3000)
    ger = Gerente("Lucas", 5000, "RH")
    dev = Desenvolvedor("Daniel", 3500, "Python")

    print(func.exibirDados())
    print(ger.exibirDados())
    print(dev.exibirDados())