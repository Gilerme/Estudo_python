import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

def SerieTitle():
    titulo = []
    for i in range(len(conteudo["data"]["series"])):
        titulo.append(conteudo["data"]["series"][i]["title"])
    return titulo

print(SerieTitle())