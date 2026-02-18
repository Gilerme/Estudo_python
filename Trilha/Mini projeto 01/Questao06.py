import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

plataforma_filme = []
plataforma_serie = []
streamings = ["Netflix", "Amazon Prime", "HBO Max", "Hulu"]

for i in range(len(conteudo["data"]["movies"])):
    for j in range(len(streamings)):
        if streamings[j] in conteudo["data"]["movies"][i]["streaming"]:
            plataforma_filme.append(streamings[j])
    
for i in range(len(conteudo["data"]["series"])): 
    for j in range(len(streamings)):
        if  streamings[j]  in conteudo["data"]["series"][i]["streaming"]:
            plataforma_serie.append("Netflix")

print(f"Plataformas de filmes disponíveis: {plataforma_filme}\n")
print(f"Plataformas de série disponíveis: {plataforma_serie}")