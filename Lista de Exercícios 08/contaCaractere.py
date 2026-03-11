def verificaChar(a):
    dicio = {}
    for i in a:
        if i in dicio:
            dicio[i] = dicio[i] + 1
        else:
            dicio[i] = 1
    return dicio


def main():
    stg = input("Digite uma string: ")
    print(verificaChar(stg))

if(__name__ == "__main__"):
    main()