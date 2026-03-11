matriz = [[None] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Digite os valores da matriz: "))
print(matriz)

for i in range(3):
   aux = matriz[1][i]
   matriz[1][i] = matriz[i][1]
   matriz[i][1] = aux
print(matriz)