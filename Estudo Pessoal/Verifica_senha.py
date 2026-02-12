senha = input("Cadastre sua senha: ")
verifica_senha = input("Digite sua senha: ")

if verifica_senha == senha:
    print("Acesso liberado")
else:
    cont = 3
    while cont > 0:
        print(f"Senha incorreta, tente novamente\n Você tem mais {cont} tentativas")
        verifica_senha = input("Digite sua senha: ")
        cont = cont -1
        if verifica_senha == senha:
            print("Acesso liberado")
            break
        elif cont == 0:
            print("Acesso bloqueado")
    

