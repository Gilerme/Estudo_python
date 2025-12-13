''' Programa verifica se numero eh impar e multiplo de 3 em 
um conjuto de 1 a 100 e faz a soma caso seja verdade'''
soma = 0
valor = 1

while(valor <= 500):
    if(valor % 2 == 1 and valor % 3 == 0):
        soma += valor
        print(valor)
    valor += 1
print(soma)