import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)
ano = { }
nominados = []
for i in range(len(conteudo["data"]["movies"])):

    for j in range(len(conteudo["data"]["movies"][i]["awards"])):
        
        ano[conteudo["data"]["movies"][i]["awards"][j]["year"]] =  conteudo["data"]["movies"][i]["awards"][j]["nominees"]

print(ano)
