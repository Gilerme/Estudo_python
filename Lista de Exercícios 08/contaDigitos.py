def contaDigitos(a):
    a = str(a)
    cont = 0
    if a[0] == "-":
        for i in range(len(a)):
            cont += 1
        return cont - 1
    else:
         for i in range(len(a)):
            cont += 1
            return cont


def main():
    num = int(input("Digite um valor: "))
    print(f"O número digitado tem {contaDigitos(num)} digítos")  


if(__name__ == "__main__"):
    main()
