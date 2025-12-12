lado1 = float(input("Informe o primeiro lado do triângulo: "))
lado2 = float(input("Informe o segundo lado do triângulo: "))
lado3 = float(input("Informe o terceiro lado do triângulo: "))

#Iniciando as condições para verificação do tipo do triângulo
if(lado1 == lado2 and lado1 == lado3):
    print("O trinângulo é equilátero")
elif(lado1 == lado2 or lado1 ==lado3 or lado2 == lado3):
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")