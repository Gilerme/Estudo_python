import random
n = 0 
d1 = d2 = d3 = d4 = d5 = d6 = 0
dado = []
n = int(input("Quantas vezes o dado foi lançado?: "))
if n > 0:
    for i in range(n):
        dado.append(random.randint(1,6))
        if dado[i] == 1:
            d1 += 1
        elif dado[i] == 2:
            d2 += 1
        elif dado[i] == 3:
            d3 += 1
        elif dado[i] == 4:
            d4 += 1
        elif dado[i] == 5:
            d5 += 1
        else:
            d6 += 1
    print(dado)
    print("Porcentagem das faces")
    print(f"1: {d1 / 100}\n2: {d2 / 100}\n3: {d3 / 100}\n4: {d4 / 100}\n5: {d5 / 100}\n6: {d6 / 100}")
    