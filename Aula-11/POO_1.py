class person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def cumprimentar(self):
        '''Função para printar uma saudação utilizando o nome da pessoa
        '''
        print(f"Olá, meu nome é {self.nome}")

p1 = person("Daniel", 24)
p2 = person("Geovana", 22)
p3 = person("Marcos", 61)

persons = [p1, p2, p3]

for p in persons:
    print(p.nome)
    print(p.idade)
    print(10*"=")

for p in persons:
    p.cumprimentar()
    print("="*10)