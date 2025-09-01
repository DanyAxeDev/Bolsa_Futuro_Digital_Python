from funcaoMedia import media

def mediaAlunos(nome, notas = []):
    m = media(notas)
    if(m > 6):
        situacao = "foi aprovado"
    elif(5 <= m < 6):
        situacao = "está de recuperação"
    else:
        situacao = "foi reprovado"
    return f"Olá, {nome}, sua média foi {m}, e você {situacao}"

if __name__ == '__main__':
    notas = []
    nome = input("Digite seu nome: ")
    while True:
        n = float(input("Digite sua nota: "))
        notas.append(n)

        parar = input("Tem mais alguma nota? (s / n): ")
        
        if(parar == "n"):
            break
    
    print(mediaAlunos(nome, notas))
        
