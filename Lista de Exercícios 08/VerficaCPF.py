def verificacpf(a):
 
#transformação da string em lista
    cont = 0
    l = []
    while cont < len(a):
        if a[cont] == "." or a[cont] == "-":
            cont += 1
        else:
            l.append(int(a[cont]))
            cont += 1

#verificação do digito j
    cont = 10
    j = 0
    for i in range(9):
        j = j + (l[i] * cont)
        cont -= 1
    if (j % 11 < 2):
        j = 0
    else:
        j = 11 - (j % 11)
    
#verificação do digito k
    cont = 11
    k = 0
    for i in range(10):
        k = k + (l[i] * cont)
        cont -= 1
    if (k % 11 < 2):
        k = 0
    else:
        k = 11 - (k % 11)

#validação do CPF
    if(j == l[9] and k == l[10]):
        return True
    else:
        return False




def main():
    cpf = input("Digite o CPF(xxx.xxx.xxx-xx): ")
    if(verificacpf(cpf)):
        print("CPF válido")
    else:
        print("CPF inválido")
    


if(__name__ == "__main__"):
    main()