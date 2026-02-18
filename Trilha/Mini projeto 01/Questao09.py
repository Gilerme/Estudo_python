import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

ator = []
personagem = []

for i in range (len(conteudo["data"]["movies"])):
    for j in range(len(conteudo["data"]["movies"][i]["cast"])):
        ator.append(conteudo["data"]["movies"][i]["cast"][j]["actor"])
        personagem.append(conteudo["data"]["movies"][i]["cast"][j]["character"])

for i in range(len(conteudo["data"]["series"])):
    for j in range (len(conteudo["data"]["series"][i]["cast"])):
        ator.append(conteudo["data"]["series"][i]["cast"][j]["actor"])
        personagem.append(conteudo["data"]["series"][i]["cast"][j]["character"])

print("Lista de atores e seus pernagens: ")
for k in range (len(ator)):
    print(f"Ator: {ator[k]} - personagem: {personagem[k]}")