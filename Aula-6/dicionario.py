aluno = {
    "nome": "Daniel",
    "idade": 24,
    "nota": {
        1: 8.5,
        2: 9.0,
        3: 7.5
    },
    "curso": "Python"
}

for key in aluno:
    print(f"{key}: {aluno[key]}")

for key, value in aluno.items():
    print(f"{key}: {value}")

for key in aluno.keys():
    print(f"Chave: {key}")

for value in aluno.values():
    print(f"Valor: {value}")

for key, value in aluno.items():
    if key == "nota":
        media = sum(value.values()) / len(value)
        print(f"Média de {key}: {media:.1f}")
