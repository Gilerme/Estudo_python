import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

lista = []
if conteudo["data"]["movies"][0]["streaming"]["Netflix"]["available"] == 1:
    if "4K" in conteudo["data"]["movies"][0]["streaming"]["Netflix"]["resolution"]:
        lista.append(conteudo["data"]["movies"][0]["title"])

if conteudo["data"]["movies"][0]["streaming"]["Amazon Prime"]["available"] == 1:
    if "4K" in conteudo["data"]["movies"][0]["streaming"]["Amazon Prime"]["resolution"]:
        lista.append(conteudo["data"]["movies"][0]["title"])
        
if conteudo["data"]["series"][0]["streaming"]["Netflix"]["available"] == 1:
    if "4K" in conteudo["data"]["series"][0]["streaming"]["Netflix"]["resolution"]:
        lista.append(conteudo["data"]["series"][0]["title"])
    
print(f"Lista de filmes e séries em resolução 4K: {lista}")