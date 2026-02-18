import json
with open("movies_and_series.json") as arquivo:
    conteudo = json.load(arquivo)

movie_rating = 0
serie_rating = 0
for i in range(len( conteudo["data"]["movies"])):
    if( movie_rating <  conteudo["data"]["movies"][i]["rating"]):
        movie_rating =  conteudo["data"]["movies"][i]["rating"]
        filme =  conteudo["data"]["movies"][i]["title"]

for j in range(len( conteudo["data"]["series"])):
    if( serie_rating <  conteudo["data"]["series"][j]["rating"]):
        serie_rating =  conteudo["data"]["series"][j]["rating"]
        serie =  conteudo["data"]["series"][j]["title"]
if movie_rating > serie_rating:
    print(f"O filme {filme} contém maior valor de rating com {movie_rating} pontos")
else:
    print(f"A serie {serie} contém maior valor de rating com {serie_rating} pontos")