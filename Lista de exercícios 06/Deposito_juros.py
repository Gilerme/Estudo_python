deposito = int(input("Digite o valor de depósito: "))
juros = float(input("Digite a taxa de juros da poupança: "))
ganhos = deposito

print("Valores nos primeiros 24 meses: ")

for i in range(1,25):
    ganhos = ganhos + deposito * (juros / 100)
    print(f"mês {i}: R${ganhos}")

print(f"O total de ganhos foi de: R${ganhos}")