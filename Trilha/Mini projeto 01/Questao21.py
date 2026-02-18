import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)
comment = []
for i in range(len(conteudo["data"]["movies"])):
    for j in range(len(conteudo["data"]["movies"][i]["reviews"])):
        date = int(conteudo["data"]["movies"][i]["reviews"][j]["details"]["date"].replace("-",""))
        if date < 20220101:
            comment.append(conteudo["data"]["movies"][i]["reviews"][j]["comment"])

for i in range(len(conteudo["data"]["series"])):
    for j in range(len(conteudo["data"]["series"][i]["reviews"])):
        date = int(conteudo["data"]["series"][i]["reviews"][j]["details"]["date"].replace("-",""))
        if date < 20220101:
            comment.append(conteudo["data"]["series"][i]["reviews"][j]["comment"])
print(f"Lista de comentários feitos antes de 2022:\n {comment}")