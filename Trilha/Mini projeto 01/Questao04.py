import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

genero = []
for i in range(len(conteudo["data"]["movies"])):
    for j in range(len(conteudo["data"]["movies"][i]["genres"])):
        if conteudo["data"]["movies"][i]["genres"][j] not in genero:
            genero.append(conteudo["data"]["movies"][i]["genres"][j])

for i in range(len(conteudo["data"]["series"])):
    for j in range(len(conteudo["data"]["series"][i]["genres"])):
        if conteudo["data"]["series"][i]["genres"][j] not in genero:
            genero.append(conteudo["data"]["series"][i]["genres"][j])

print(genero)