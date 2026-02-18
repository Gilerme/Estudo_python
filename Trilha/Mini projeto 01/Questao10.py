import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

salario = 0

for i in range (len(conteudo["data"]["movies"])):
    for j in range(len(conteudo["data"]["movies"][i]["cast"])):
        if conteudo["data"]["movies"][i]["cast"][j]["salary"] > salario:
            salario = conteudo["data"]["movies"][i]["cast"][j]["salary"]
            ator = (conteudo["data"]["movies"][i]["cast"][j]["actor"])

for i in range (len(conteudo["data"]["series"])):
    for j in range(len(conteudo["data"]["series"][i]["cast"])):
        if conteudo["data"]["series"][i]["cast"][j]["salary"] > salario:
            salario = conteudo["data"]["series"][i]["cast"][j]["salary"]
            ator = (conteudo["data"]["series"][i]["cast"][j]["actor"])

print(f"O ator com maior salário é: {ator}\n Salário: R${salario:.2f}")