import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)


for i in range (len(conteudo["data"]["movies"])):
   domestic = conteudo["data"]["movies"][i]["production"]["boxOffice"]["ticketSales"]["domestic"]
   international = conteudo["data"]["movies"][i]["production"]["boxOffice"]["ticketSales"]["international"]
   filme = conteudo["data"]["movies"][i]["title"]
   print(f"Filme: {filme}\n vendas domésticas: {domestic} - vendas internacionais: {international}")