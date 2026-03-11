def forca(a):
    import random
    palavras = ("desodorante", "perfume", "oculos", "livro")
    jogo = random.choice(palavras)
    l = ["-"] * (len(jogo))
    cont = 1
    while cont <= 6:
        if a in jogo:
            for i in range(len(jogo)):
                if a == jogo[i]:
                    l[i] = a
            
            print("\n",l)
            
            if "-" not in l:
                return l
            a = input("Digite uma letra: ")
        else:   
            if cont == 6:
                return False
            
            else:
                print(f"Você errou pela {cont}ª vez")
                print("Tente novamente!")
                a = input("Digite uma letra: ")
                cont += 1 


def main():
    print("--------JOGO DA FORCA--------")
    letra = input("Digite uma letra: ")
    palavra = forca(letra)
    if palavra != False:
        print(f"Parabéns, a palavra era {''.join(palavra)}")
    else:
        print("Você perdeu o jogo!")





if (__name__ == "__main__"):
    main()