import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

for i in range(len(conteudo["data"]["movies"])):
   for j in range(len(conteudo["data"]["movies"][i]["awards"])):
        year = conteudo["data"]["movies"][i]["awards"][j]["year"]
        award = conteudo["data"]["movies"][i]["awards"][j]["award"]
        category = conteudo["data"]["movies"][i]["awards"][j]["category"]

   print(f"Prêmios de filmes:\n Nome: {award} - Ano: {year} - categoria: {category}\n")

for i in range(len(conteudo["data"]["series"])):
    for j in range(len(conteudo["data"]["movies"][j]["awards"])):
        year = conteudo["data"]["series"][j]["awards"][j]["year"]
        award = conteudo["data"]["series"][j]["awards"][j]["award"]
        category = conteudo["data"]["series"][j]["awards"][j]["category"]

    print(f"Prêmios de séries:\n Nome: {award} - Ano: {year} - categoria: {category}\n")