import funcoes

def main():
    l = []
    a = float(input("Digite um valor da lista (-1 para sair): "))
    while (a != -1):
        l.append(a)
        a = float(input("Digite um valor da lista (-1 para sair): "))
    print(f"A média e o desvio da lista são respectivamente {funcoes.mediaDesvio(l)}")

if (__name__ == "__main__"):
    main()