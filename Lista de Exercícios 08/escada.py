def main():
    stg = input("Digite uma string: ")
    i = 0 
    b = ""
    while i < len(stg):
        b = b + stg[i]
        i += 1
        print(b)
        


if(__name__ == "__main__"):
    main()