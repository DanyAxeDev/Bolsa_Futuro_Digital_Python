def media(n = []):
    return sum(n)/len(n)

if __name__ == '__main__':

    lista = []

    while True:
        n = int(input("Digite um valor para compor a média: "))
        lista.append(n)

        parar = input("Deseja parar? (s / n): ")

        if(parar == "s"):
            break
            
    print(f"A média dos números passados é {media(lista)}")

