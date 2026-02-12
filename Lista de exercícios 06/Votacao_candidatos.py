eleitores = int(input("Digite a quantidade total de eleitores: "))
votoA = 0
votoB = 0
votoC = 0
votoN = 0
for i in range (1,eleitores+1):
    print("Em quem você vota?\n 1 - candidato A\n 2 - candidato B\n 3 - candidato C")
    voto = int(input())
    if(voto == 1):
        votoA += 1
    elif(voto == 2):
        votoB += 1
    elif(voto == 3):
        votoC += 1
    else: 
        print("Voto inválido")
        votoN += 1
print(f"Resultado final:\n canditado A: {votoA} votos\n candidato B: {votoB} votos\n candidato C: {votoC} votos\n votos inválidos: {votoN} votos")