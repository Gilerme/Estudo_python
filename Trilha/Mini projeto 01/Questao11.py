import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

locacoes = []
for i in range(len(conteudo["data"]["movies"])):
    for j in range (len(conteudo["data"]["movies"][i]["production"]["filmingLocations"])):
        locacoes.append(conteudo["data"]["movies"][i]["production"]["filmingLocations"][j])

print(f"Localizações de filmagens: {locacoes}")