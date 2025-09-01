def div(i, j):
    if(j == 0):
        print("O valor do divisor não pode ser 0")
        return False
    else:
        return i/j
    
if __name__ == '__main__':
    i = float(input("Digite um número: "))
    j = float(input("Digite o número que irá dividir o primeiro: "))

    r = div(i, j)

    if(r):
        print(f"A divisão de {i} por {j} é {r:.2f}")