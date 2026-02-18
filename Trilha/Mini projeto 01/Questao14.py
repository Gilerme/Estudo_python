import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

lucro = 0
cont = 0

for i in range (len(conteudo["data"]["movies"])):
  lucro = conteudo["data"]["movies"][i]["production"]["boxOffice"]["revenue"]
  cont += 1
print(f"A média de lucro é: {lucro / cont}")
