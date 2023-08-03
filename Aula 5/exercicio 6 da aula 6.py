def situação(n):
    if n >= 6:
        return "Verdadeiro"  #aprovado
    else:
        return "Falso"  #reprovado

def main():
    nota1 = int(input("Digite a nota do primeiro bimestre:"))
    nota2 = int(input("Digite a nota do segundo bimestre:"))
    nota3 = int(input("Digite a nota do terceiro bimestre:"))
    nota4 = int(input("Digite a nota do quarto bimestre:"))
    media = (nota1 + nota2 + nota3 + nota4)//4
    print(situação(media))

main()
    
