def real(n):
    while True:
        try:
            return float(n)
        except:
            print(f"{n} não é um número real, tente novamente!")
            n = input("Digite a nota do bimestre:")

def main():
    nota1 = real(input("Digite a nota do primeiro bimestre:"))
    nota2 = real(input("Digite a nota do segundo bimestre:"))
    nota3 = real(input("Digite a nota do terceiro bimestre:"))
    nota4 = real(input("Digite a nota do quarto bimestre:"))
    media = (nota1 + nota2 + nota3 + nota4)// 4
    print("Média final do aluno:", media)
        
#################PRINCIPAL###############################################      
main()


