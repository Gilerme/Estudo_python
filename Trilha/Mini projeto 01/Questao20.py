import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

cont = 0
for i in range(len(conteudo["data"]["movies"])):
    rating = conteudo["data"]["movies"][i]["rating"]
    cont += 1
print(f"A média de notas dos filmes é: {rating / cont}")