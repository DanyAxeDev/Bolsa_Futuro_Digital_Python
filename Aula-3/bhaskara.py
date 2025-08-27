a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

print(f"Resolvendo a equação do segundo grau: {a}x² + {b}x + {c} = 0")

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2*a)
    print(f"A equação possui uma raiz real: {x}")
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(f"As raízes da equação são: {x1} e {x2}")