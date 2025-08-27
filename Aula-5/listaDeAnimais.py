animais = ["Cachorro", "Gato", "Pássaro", "Peixe", "Coelho"]

print("\nLista de Animais Original:", end=" ")
for i, animal in enumerate(animais):
    print(animal, end=" -> " if i != len(animais) - 1 else "\n")

animais.pop(2)

print("\nLista de Animais Após Remoção:", end=" ")
for i, animal in enumerate(animais):
    print(animal, end=" -> " if i != len(animais) - 1 else "\n\n")