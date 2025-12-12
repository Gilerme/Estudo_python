preco = float(input("Informe o preço do produto: "))
forma_pagamento = input("Informe a forma de pagamento:")

if(preco >= 100 and forma_pagamento == "dinheiro"):
    preco = preco * 0.9
    print(f"O novo preço a ser pago é R${preco:.2f}")
elif(forma_pagamento == "cheque"):
    print(f"O valor a ser pago é R${preco:.2f}")
elif(forma_pagamento == "cartão"):
    funcao_cartao = input("Informe se é débito ou crédito: ")
    if(funcao_cartao == "débito"):
       print(f"O valor a ser pago é R${preco:.2f}")
    elif(funcao_cartao == "crédito"):
        parcela_cartao = int(input("Informe o número de parcelas: "))
        if(parcela_cartao > 0 and parcela_cartao <= 3):
            print(f"O valor a ser pago é R${preco:.2f}")
            print(f"{parcela_cartao} parcelas de R${preco/parcela_cartao:.2f}")
        else:
            print("Quantidade de parcelas inválida")
elif(preco < 100):
    print(f"O valor a ser pago é R${preco:.2f}")
else:
    print("Forma de pagamento inválida")
