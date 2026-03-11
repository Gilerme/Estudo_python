altura = []
sexo = []
for i in range(10):
    altura.append(float(input("Digite a altura da pessoa: ")))
    sexo.append(input("Digite o sexo da pessoa(M/F): "))

maior = menor = 0
sexoM = sexoF = "N/A"
for i in range(10):
    if altura[i] > maior:
        maior = altura[i] 
    elif altura[i] < menor:
        menor = altura[i]

#verificando a maior e a menor altura
for i in range(10):
    if altura[i] == maior:
        print(f"\nA maior altura é {altura[i]} e o sexo da pessoa é {sexo[i]}")
    elif altura[i] == menor:
        print(f"A menor altura é {altura[i]} e o sexo da pessoa é {sexo[i]}\n")

#Média de altura entre homens e mulheres
mediaM = mediaF = 0
contM = contF = 0
for i in range(10):
    if sexo[i] == "M":
        mediaM += altura[i]
        contM += 1
    else:
        mediaF += altura[i]
        contF += 1
print(f"\nA média de altura entre os homens é {mediaM / contM}")
print(f"A média de altura entre as mulheres é {mediaF / contF}\n")

#Número total de indivíduos de cada sexo
contF = contM = 0
for i in range(10):
    if sexo[i] == "M":
        contM += 1
    else:
        contF += 1
print(f"O número de homens é: {contM}\nO número de mulheres é: {contF}")