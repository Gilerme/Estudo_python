import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)
    
quantidade = 0
i = 0
j = 0

while i < len(conteudo["data"]["movies"]):
    if "id" in conteudo["data"]["movies"][i]:
        quantidade += 1
    i += 1

while j < len(conteudo["data"]["series"]):

    if "id" in conteudo["data"]["series"][j]:
        quantidade += 1
    j += 1

print(quantidade)
   