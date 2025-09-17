class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, me chamo {self.nome} e tenho {self.idade} anos. "
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    def apresentar(self):
        return super().apresentar() + f"Estou no curso de {self.curso}"
    
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

    def apresentar(self):
        return super().apresentar() + f"Sou professor na disciplina {self.disciplina}"
    
if __name__ == "__main__":
    p1 = Pessoa("Geovana", 22)
    a1 = Aluno("Daniel", 24, "202202856691", "Python")
    pr1 = Professor("Ronaldo", 40, "Python", 3000)

    pessoas = [p1, a1, pr1]

    for pessoa in pessoas:
        print(pessoa.apresentar())