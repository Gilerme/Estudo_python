n = int(input("Quantos números da sequência Fibonacci você deseja ver: "))
anterior = 0
atual = 1
fibonacci = anterior + atual
print(fibonacci)
for i in range (n-1):
    print(fibonacci)
    anterior = atual
    atual = fibonacci
    fibonacci = anterior + atual
   
    

    
   
   