maior = 0
menor = 0
soma = 0

valor = float(input("(Digite -1 para sair) \nDigite um valor: "))
menor = maior = valor

while(valor != -1):
    if (valor > maior):
        maior = valor
    elif(valor < menor):
        menor = valor
    soma += valor
    valor = float(input("(Digite -1 para sair) \nDigite um valor: "))
print("\n O menor valor é: %.2f \n A maior valor é: %.2f \n A soma dos números é: %.2f" % (menor,maior,soma))