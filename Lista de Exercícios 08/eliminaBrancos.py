def limpaBrancos(a):
    b = ""
    i = 0
    while i < len(a):
        if a[i] == " ":
            i += 1
        else:
            b = b + a[i]
            i += 1
    return b


def main():
    stg = input("Digite de uma string: ")
    limp = limpaBrancos(stg)
    print(limp)


if(__name__ == "__main__"):
    main()