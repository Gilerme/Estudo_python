import funcoes


def main():
    n = int(input("Digite um valor: "))
    primo = funcoes.primo(n)
    if (primo):
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")


if(__name__ == "__main__"):
    main()