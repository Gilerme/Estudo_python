def verificaMes(a):
    meses = ("","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")
    mes = int(a[3:5])
    if(mes > 0 and mes < 13):
        return(meses[mes])
    else:
        return False

def main():
    nasc = input("Digite a data de nascimento(dd/mm/aaaa): ")
    mes = verificaMes(nasc)
    dia = nasc[0:2]
    ano = nasc[6:]
    if(mes > 0 and mes < 13):
        print(f"{dia} de {mes} de {ano}")
    else:
        print("Mês não existente")


if(__name__ == "__main__"):
    main()