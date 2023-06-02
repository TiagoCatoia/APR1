def somar(n1,n2):
    return n1 + n2
def subtrair(n1,n2):
    return n1 - n2
def multiplicar(n1,n2):
    return n1 * n2
def dividir(n1,n2):
    if n2 != 0:
        return n1/n2
    else:
        return -1
def potencia(base,expoente):
    return base**expoente
def raiz_quadrada(num):
    import math
    return math.sqrt(num)
def main():
    print("Menu de opções")
    print("1. Soma de dois valores")
    print("2. Subtração de dois valores")
    print("3. Multiplicação de dois valores")
    print("4. Divisão de dois valores")
    print("5. Potenciação de dois valores")
    print("6. Raíz quadrada de um valor")
    print("7. Sair")
    op = int(input("Escolha uma opção:"))
    while op != 7:
        if op == 6:
            num = int(input("Digite um valor:"))
            print("Raíz quadrada:",raiz_quadrada(num))
        else:
            n1 = int(input("Digite o primeiro valor:"))
            n2 = int(input("Digite o segundo valor:"))
            if op == 1:
                print("Soma dos valores:",somar(n1,n2))
            elif op == 2:
                print("Subtração dos valores:",subtrair(n1,n2))
            elif op == 3:
                print("Multiplicação dos valores:",multiplicar(n1,n2))
            elif op == 4:
                if dividir(n1,n2) != -1:
                    print("Divisão dos valores:",dividir(n1,n2))
                else:
                    print("Não é possível divisão por zero!")
            else:  #op = 5
                print("Potenciação dos valores",potencia(n1,n2))
        op = int(input("Escolha uma outra opção:"))

################################PRINCIPAL#####################################################################################
main()
