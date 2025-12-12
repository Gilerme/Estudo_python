num = int(input("DIgite o primeiro número: "))
num2 = int(input("DIgite o segundo número: "))


if (num % num2 == 0 or num2 % num == 0):
    print(f"{num} e {num2} São mutiplos")
else: 
    (print(f"{num} e {num2} Não são multiplos"))