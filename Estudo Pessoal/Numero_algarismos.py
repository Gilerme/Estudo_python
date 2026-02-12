numero = int(input("Digite um número: "))
cont = 1
while numero // 10 != 0:
    cont += 1
    numero = numero // 10
print(cont)