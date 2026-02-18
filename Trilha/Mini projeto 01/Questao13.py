import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

receita = 0

for i in range (len(conteudo["data"]["movies"])):
   if receita < conteudo["data"]["movies"][i]["production"]["boxOffice"]["revenue"]:
       receita = conteudo["data"]["movies"][i]["production"]["boxOffice"]["revenue"]
       filme = conteudo["data"]["movies"][i]["title"]

print(f"O filme com maior bilheteria é: {filme}\n Bilheteria ${receita:.2f}")

