import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

def MovieTitle():
    titulo = []
    for i in range(len(conteudo["data"]["movies"])):
        titulo.append(conteudo["data"]["movies"][i]["title"])
    return titulo

print(MovieTitle())