def filmeDict(titulo, ano, diretor):
    return {"titulo": titulo, "ano": ano, "diretor": diretor}

filmesFav = [
    filmeDict("kung fu panda", "2008", "mark osborne"),
    filmeDict("Os sem florestas", "2006", "Karey Kirkpatrick"),
    filmeDict("ilha do medo", "2010", "Martin Scorsese")
]

print("Lista de filmes favoritos")
print("-"*20)
for filme in filmesFav:
    for key, value in filme.items():
        print(f"{key}: {value.capitalize()}")
    print("-"*20)