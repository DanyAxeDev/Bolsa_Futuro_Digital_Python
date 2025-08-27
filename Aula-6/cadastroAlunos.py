aluno_1 = {
    "nome": "daniel",
    "idade": 24,
    "curso": "python"
}

aluno_2 = {
    "nome": "rafael",
    "idade": 22,
    "curso": "java"
}

aluno_3 = {
    "nome": "larissa",
    "idade": 21,
    "curso": "javascript"
}

alunos = [aluno_1, aluno_2, aluno_3]

ordenacaoIdade = False

if(ordenacaoIdade):
    alunosOrdenados = sorted(alunos, key=lambda a: a["idade"])
else:
    alunosOrdenados = sorted(alunos, key=lambda a: a["nome"])

print("-" *20)
for aluno in alunosOrdenados:
    for key, value in aluno.items():
        print(f"{key}: {value}")
    print("-"*20)