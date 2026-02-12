print("<1> Depositar\n<2> Sacar\n<3> Consultar Saldo\n<4> Sair")
cod = input("Digite o valor da opção: ")
saldo = 0
while cod != "4":
    if cod == "1":
        deposito = float(input("Digite o valor para depósito: "))
        saldo = saldo + deposito
        print("\n<1> Depositar\n<2> Sacar\n<3> Consultar Saldo\n<4> Sair")
        cod = input("Digite o valor da opção: ")
    elif cod == "2":
        saque = float(input("Digite o valor para saque: "))
        if saque > saldo:
            print("Saldo insuficiente para a quantida desejada.")
            print("\n<1> Depositar\n<2> Sacar\n<3> Consultar Saldo\n<4> Sair")
            cod = input("Digite o valor da opção: ")
        else:
            saldo = saldo - saque
            print("\n<1> Depositar\n<2> Sacar\n<3> Consultar Saldo\n<4> Sair")
            cod = input("Digite o valor da opção: ")
    elif cod == "3":
        print("Seu saldo é de R$%.2f" %saldo)
        print("\n<1> Depositar\n<2> Sacar\n<3> Consultar Saldo\n<4> Sair")
        cod = input("Digite o valor da opção: ")
    else:
        print("Código inválido")
        print("\n<1> Depositar\n<2> Sacar\n<3> Consultar Saldo\n<4> Sair")
        cod = input("Digite o valor da opção: ")
