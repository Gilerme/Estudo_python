def soma(a,b,c):
    return(a + b + c)

def main():
    resultado = 0
    n1 = float(input("Digite um valor para soma: "))
    n2 = float(input("Digite um valor para soma: "))
    n3 = float(input("Digite um valor para soma: "))
    resultado = soma(n1,n2,n3)
    print("O resultado da soma é:",resultado)

if (__name__ == "__main__"):
    main()