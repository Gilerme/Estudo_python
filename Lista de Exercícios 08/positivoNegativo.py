def PN (a):
    if a > 0:
        return "P"
    else:
        return "N"
    


def main():
    var = float(input("Digite um número: "))
    if (PN(var) == "P"):
        print("Positivo")
    else:
        print("Negativo")

if (__name__ == "__main__"):
    main()