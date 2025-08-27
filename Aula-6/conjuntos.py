A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
c = {7, 8}

# União
C = A | B
print("União:", C)

# Interseção
D = A & B
print("Interseção:", D)

# Diferença
E = A - B
print("Diferença:", E)

# Diferença Simétrica
F = A ^ B
print("Diferença Simétrica:", F)

# Subconjuntos
G = A <= B
print("G:", G)

H = c <= B
print("H:", H)