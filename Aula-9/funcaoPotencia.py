def pot(n, p):
    return n**p
    

if __name__ == '__main__':
    n = int(input("Digite um número: "))
    p = int(input("Digite a qual potencia elevar o primeiro número: "))

    print(f"O número {n} elevado a {p} é igual a {pot(n,p)}")