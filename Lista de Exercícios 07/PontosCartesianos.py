
N = int(input("Digite a quantidade de pontos: "))
pontos = []
 
for i in range(N):
    x = float(input("Digite a coordenada x do ponto"[i]))
    y = float(input("Digite a coordenada y do ponto"[i]))
    pontos.append((x, y))

if N < 2:
    print("É necessário pelo menos dois pontos")
else:
    primeira = True
    soma = 0
    cont = 0  

    for i in range(N):
        for j in range(N):
            x1 = pontos[i][0]
            y1 = pontos[i][1]
            x2 = pontos[j][0]
            y2 = pontos[j][1]
            
            distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
            
            if primeira:
                minimo = distancia
                maximo = distancia
                primeira = False
            else:
                if distancia < minimo:
                    minimo = distancia
                if distancia > maximo:
                    maximo = distancia
            
            soma = soma + distancia
            cont = cont + 1
    
    media = soma / cont
    
    print("\nResultados:")
    print(f"Distância mínima: {minimo}")
    print(f"Distância máxima:{maximo}")
    print(f"Distância média:{media}")