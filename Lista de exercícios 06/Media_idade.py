idade = int(input("Digite a idade da pessoa (-1 para sair): "))
if (idade > -1):
    cont = 1
    media =  (idade / cont) 
    while(idade != -1):
        if (idade > -1):
            cont =+ 1
            media =  (idade / cont)
            idade = int(input("\nDigite a idade da pessoa (-1 para sair): "))
        elif(idade < -1):
            print("Idade inválida\n") 
            idade = int(input("Digite a idade da pessoa (-1 para sair): "))
    if (media > 0 and media <= 25):
        print(f"A turma é jovem")
    elif (media > 25 and media <= 60):
         print(f"A turma é adulta")
    elif (media > 60):
         print(f"A turma é idosa")
         
elif(idade < -1):
    print("Idade inválida")

