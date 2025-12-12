valor_hora = float(input("digite o quanto ganha por hora: "))

horas_trabalho = float(input("\nDigite quantas horas você trabalhou nesse mês: "))

salario = valor_hora*horas_trabalho

# resultado do salario com os descontos
print(f"Sálario Bruto: {salario}\n IR(11%): {0.11*salario}\n INSS(8%):{0.08*salario}\n Sindicato(5%): {0.05*salario}\n Salário Líquido: {0.76*salario}")