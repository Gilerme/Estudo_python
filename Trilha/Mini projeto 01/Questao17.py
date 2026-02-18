import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)
filme = []
serie = []
for i in range(len(conteudo["data"]["movies"])):
    for j in range(len(conteudo["data"]["movies"][i]["awards"])):
        if conteudo["data"]["movies"][i]["awards"][j]["won"] == 1:
            filme.append(conteudo["data"]["movies"][i]["title"])
print("Lista de filmes premiados:")
for k in range(len(filme)):
    print(filme[k])

for i in range(len(conteudo["data"]["series"])):
    for j in range(len(conteudo["data"]["series"][i]["awards"])):
        if conteudo["data"]["series"][i]["awards"][j]["won"] == 1:
            serie.append(conteudo["data"]["series"][i]["title"])
print("Lista de séries premiados:")
for k in range(len(serie)):
    print(serie[k])