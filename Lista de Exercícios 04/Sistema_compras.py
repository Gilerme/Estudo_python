codigo = int(input("Digite o código do produto(0 para sair): "))
total = 0
while (codigo != 0):
    if (codigo == 1):
        quant = int(input("Digite a quantidade comprada: "))
        total += quant * 5.5
        codigo = int(input("Digite o código do produto(0 para sair): "))
    elif (codigo == 2):
        quant = int(input("Digite a quantidade comprada: "))
        total += quant * 2.3
        codigo = int(input("Digite o código do produto(0 para sair): "))
    elif (codigo == 3):
        quant = int(input("Digite a quantidade comprada: "))
        total += quant * 4.75
        codigo = int(input("Digite o código do produto(0 para sair): "))
    elif (codigo == 4):
        quant = int(input("Digite a quantidade comprada: "))
        total += quant * 6.80
        codigo = int(input("Digite o código do produto(0 para sair): "))
    elif (codigo == 5):
        total += quant * 9.30
        quant = int(input("Digite a quantidade comprada: "))
        codigo = int(input("Digite o código do produto(0 para sair): "))
    else:
        print("Código inválido")
        break
print(f"O total de compras é R${total:.2f}")