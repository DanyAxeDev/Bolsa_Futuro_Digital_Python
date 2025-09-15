class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def __str__(self):
        return f"O nome do funcionário é {self.nome} e seu salário é R${self.__salario}"
    
    def getSalario(self):
        return self.__salario
    
    def setSalario(self, valor):
        salarioAntigo = self.__salario

        if(valor > 0):
            self.__salario = valor
            diferenca = self.__salario - salarioAntigo
            print(f"Salário antigo: R${salarioAntigo}")
            print(f"Novo salário: R${self.__salario}")
            print(f"Diferença: R${diferenca}")

if __name__ == '__main__':
    f = Funcionario("Daniel", 1000)

    print(f)

    f.setSalario(2000)

    print(f)