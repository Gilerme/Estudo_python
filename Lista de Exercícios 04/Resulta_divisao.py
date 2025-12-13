num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
div_int = num1 // num2
print(f"A divisão inteira do primeiro pelo segundo é: {div_int}\n")

resto = num1 - num2

while(div_int > 0):
    div_int -= 1
    print(f"Resto da divisão: {resto}\n")
    resto -= num2
    
    
