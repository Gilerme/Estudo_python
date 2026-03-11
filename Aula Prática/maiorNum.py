import funcoes

def main():
    l = []
    a = float(input("Digite um valor da lista (-1 para sair): "))
    while (a != -1):
        l.append(a)
        a = float(input("Digite um valor da lista (-1 para sair): "))
    maior = funcoes.maiorValor(l)
    print(maior)

if(__name__ == "__main__"):
    main()