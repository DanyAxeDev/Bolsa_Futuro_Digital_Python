class Aluno:
    def __init__(self, nome, notas = []):
        self.nome = nome
        self.notas = notas
    
    def media(self):
        return (sum(self.notas))/len(self.notas)
    
    def situacao(self):
        if(self.media() >= 6):
            return "aprovado"
        elif (5 <= self.media() < 6):
            return "em recuperação"
        else:
            return "reprovado"
        
if __name__ == '__main__':
    nome = input("Olá, digite o nome do aluno: ")

    qtyNota = 1
    notas = []
    
    while True:
        continuar = input("Deseja inserir uma nota? (s / n) ")

        if(continuar == "n"):
            break

        nota = float(input(f"Digite a {qtyNota}º nota: "))
        notas.append(nota)
        qtyNota += 1

    aluno1 = Aluno(nome, notas)
    print(f"O aluno {aluno1.nome} ficou com média {aluno1.media():.1f} e portanto, está {aluno1.situacao()}")