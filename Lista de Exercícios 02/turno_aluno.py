turno = input("Informe o turno em que você estuda:\n Matutino(M)\n Vespertino(V)\n Noturno(N)\n")

if(turno == "M"):
    print("Bom Dia!")
elif(turno == "V"):
    print("Boa Tarde!")
elif(turno == "N"):
    print("Boa Noite!")
else:
    print("Valor inválido")