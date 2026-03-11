def tamanhoString (a,b):
    a = len(a)
    b = len(b)
    return(a,b)

def conteudoString (a,b):
    if a == b:
        return True
    else:
        return False

def main():
   s1 = input("Digite a primeira string: ")
   s2 = input("Digite a segunda string: ")
   tamanho = (tamanhoString(s1,s2))
   conteudo = conteudoString(s1, s2)
   
   if(tamanho[0] == tamanho[1]):
      if(conteudo):
          print(f"String 1 é {s1} e string 2 é {s2} ")
          print(f"Elas tem tamanho igual a {tamanho[0]} e conteúdo igual")
      else:
          print(f"String 1 é {s1} e string 2 é {s2} ")
          print(f"Elas tem tamanho igual a {tamanho[0]} e conteúdo diferente")
   else:
      print(f"String 1 é {s1} com tamanho {tamanho[0]}  e string 2 é {s2} com tamanho {tamanho[1]} ")
      print(f"Elas possuem o conteúdo diferente")
    


if (__name__ == "__main__"):
    main()