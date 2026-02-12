num = int(input("Digite o número que deseja saber se é primo: "))
cont = 0
if(num == 0 or num == 1):
    print(f"{num} não é primo")
else:
    for i in range(1,num+1):
        if(num % i == 0):
           cont += 1
if(cont > 2):
    print(f"{num} não é primo")
else:
    print(f"{num} é primo")
        
        