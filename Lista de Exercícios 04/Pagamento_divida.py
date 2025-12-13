divida = float(input("Digite o valor da dívida: "))
juros = float(input("Digite o juros mensal(em porcentagem): "))
pagamento = float(input("Digite o quanto deseja pagar por mês: "))

mes = 1
total_juros = 0
divida_total = divida

if(pagamento > divida * (juros / 100)):
    while (divida > 0):
        divida = divida + divida * (juros / 100) 
        total_juros += divida
        divida -= pagamento
        mes += 1
    print(f"A dívida foi paga em {mes} meses\nO total de pago foi de R${total_juros:.2f}")
    print(f"\nE o total de jutos pago foi de R${total_juros - divida_total:.2f}")
else:
    print("Sua dívida não será paga pois o valor mensal é menor que o juros")