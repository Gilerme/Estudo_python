import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

filme = []
diretor = []

for i in range (len(conteudo["data"]["movies"])):
    filme.append(conteudo["data"]["movies"][i]["title"])
    diretor.append(conteudo["data"]["movies"][i]["directors"])

for j in range (len(filme)):
    print(f"Filme: {filme[j]} - Diretor: {diretor[j]}")