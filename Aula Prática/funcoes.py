def dobra(a):
    return(2 * a)

def potencia1(a, b):
    return(a ** b)

def potencia2(a, b):
    pot = a
    for i in range(b-1):
        pot = pot * a 
    return(pot)
    
def maiorValor(a = []):
    maior = a[0]
    for i in range(len(a)):
        if  a[i] > maior:
            maior = a[i]
    return maior

def primo(num):
    if(num == 0 or num == 1):
        return(False)
    else:
        cont = 0
        for i in range(1,num+1):
            if(num % i == 0):
               cont += 1
    if(cont > 2):
        return(False)
    else:
        return(True)

def mediaDesvio(a):
    import math
    media = soma = cont = 0
    for i in range(len(a)):
        soma = soma + a[i]
        cont += 1
    media =  soma / cont

    variacao = sum((x - media)**2 for x in a) / (cont - 1)
    desvio = math.sqrt(variacao)
    return( media, " e ", desvio)
        