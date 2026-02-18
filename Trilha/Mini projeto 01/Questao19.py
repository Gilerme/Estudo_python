import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

maior = 0
for i in range(len(conteudo["data"]["movies"])):
    for j in range(len(conteudo["data"]["movies"][i]["reviews"])):
        if conteudo["data"]["movies"][i]["reviews"][j]["details"]["helpfulVotes"] > maior:
            maior = conteudo["data"]["movies"][i]["reviews"][j]["details"]["helpfulVotes"]
            user = conteudo["data"]["movies"][i]["reviews"][j]["user"]
            comment = conteudo["data"]["movies"][i]["reviews"][j]["comment"]

for i in range(len(conteudo["data"]["series"])):
    for j in range(len(conteudo["data"]["series"][i]["reviews"])):
        if conteudo["data"]["series"][i]["reviews"][j]["details"]["helpfulVotes"] > maior:
            maior = conteudo["data"]["series"][i]["reviews"][j]["details"]["helpfulVotes"]
            user = conteudo["data"]["series"][i]["reviews"][j]["user"]
            comment = conteudo["data"]["series"][i]["reviews"][j]["comment"]

print(f"O comentário com maior número de votos úteis foi:\nUsuário: {user} - Comentário: {comment} - Votos úteis {maior}")