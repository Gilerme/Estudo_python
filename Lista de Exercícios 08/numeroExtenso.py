def numeroExtenso(a):
    un = ("","um","dois","três","quatro","cinco","seis","sete","oito","nove")
    dec = ("dez","onze","doze","treze","quatorze","quize","dezesseis","dezesete","dezoito","dezenove")
    dez =("","","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitena","noventa")
    extenso = ""
    i = 0
    l = []
    while i < len(a):
        l.append(int(a[i]))
        i += 1
        
    for i in range(len(l)):
        if len(l) == 1:
            extenso = un[l[i]]
        else:
            if l[0] == 1:
                extenso = dec[l[i-1]]
                break
            if i == 0:
                extenso = dez[l[i]]
            else:
                extenso = extenso + " e " +  un[l[i]]
    return extenso

def main():
    valor = input("Digite um valor de 1 a 99: ")
    #print(len(valor))
    print(numeroExtenso(valor))

if(__name__ == "__main__"):
    main()