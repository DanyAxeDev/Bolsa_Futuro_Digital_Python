nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Xuxa", "Yara", "Zé"]


def verificar_lista(lista, letraProibida, letraPula):
    if not lista:
        return "A lista está vazia."
    else:
        print(f"A lista contém {len(lista)} elementos.")

        for i, nome in enumerate(lista):
            if nome.startswith(letraProibida):
                break
            if nome.startswith(letraPula):
                continue
            print(f"{i + 1}: {nome}")

verificar_lista(nomes, "Y", "A")