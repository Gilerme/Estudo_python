def printaN(a):
    b = str(a)
    for i in range(a):
        print(b)
        b += " " + str(a)

def main():
    num = int(input("Digite um valor inteiro: "))
    printaN(num)

if(__name__ == "__main__"):
    main()