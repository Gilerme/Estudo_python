frase = input("Digite uma frase (-1 para encerrar): ")
dicionario = {}

if frase != "-1":
    while frase != "-1":
        for i in range(len(frase)):
            caractere = frase[i]
            if caractere in dicionario:
                dicionario[caractere] = dicionario[caractere] + 1
            else:
                dicionario[caractere] = 1
        print("Dicionário da frase:")
        print(dicionario)
        print()
        frase = input("Digite uma frase (-1 para encerrar): ")
        dicionario = {}
           
  