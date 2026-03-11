codigo = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(len(codigo))
mensagem = []
numero = 0

numero = int(input("Digite a mensagem codificada número por número(-1 para sair)"))

if numero >= 0 and numero <= 26:
    while numero != -1:
        if numero >= 0 and numero <= 26:
            mensagem.append(codigo[numero])
            numero = int(input("Digite a mensagem codificada número por número(-1 para sair)"))
        else: 
            print("Número não pertence ao código")
    print(f"Mensagem decodificada: {mensagem}")
else: 
            print("Número não pertence ao código")