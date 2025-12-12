nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

#Cálculo de média aritmética
media = (nota1 + nota2)/2

#verificação de aprovação
if(media >= 9 and media <= 10):
    print("conceito A")
elif(media >=7.5):
    print("conceito B")
elif(media >= 6):
    print("conceito C")
elif(media >= 4):
    print("conceito D")
else:
    print("Conceito E")