n = float(input("Digite o valor para raiz quadrada: "))
b = 2
p =(b + (n/b))/2  
while abs(b) - abs(p) >= 0.0001:
    b = p
    p =(b + (n/b))/2
print(f"{b:.2f} é a raiz aproximada de {n}")
