preco = float(input("Informe o preço do produto: "))
forma_pagamento = input("Informe a forma de pagamento:")

if(preco >= 100 and forma_pagamento == "dinheiro"):
    preco = preco * 0.9
    print("O novo preço a ser pago é R$%.2f", preco)
elif(preco >=100 and forma_pagamento == "cheque" or preco < 100):
    print("O valor a ser pago continua o mesmo")
else:
    print("Forma de pagamento inválida")