import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

lista =[]
url = []
for i in range(len(conteudo["data"]["movies"])):
    if conteudo["data"]["movies"][i]["streaming"]["Netflix"]["available"] == 1:
        url.append(conteudo["data"]["movies"][0]["streaming"]["Netflix"]["url"])
        lista.append("Netflix")

    if conteudo["data"]["movies"][0]["streaming"]["Amazon Prime"]["available"] == 1:
        url.append(conteudo["data"]["movies"][0]["streaming"]["Amazon Prime"]["url"])
        lista.append("Amazon Prime")

print("Lista de streamings disponíveis: ")
for i in range (len(lista)):
    print(f"Streaming: {lista[i]} - URL: {url[i]}")