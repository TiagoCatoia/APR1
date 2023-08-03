def menu():
    print("\nMenu de opções:")
    print("1. Fatorial de um número")
    print("2. Fibonacci de um número")
    print("3. Soma dos elementos de um vetor/lista de determinado tamanho")
    print("4. Potência positiva de um número")
    print("5. Calcular o MDC entre dois números")
    print("0. Sair")
    op = int(input("Digite a opção desejada:"))
    while op != 0:
        if op == 1:
            return 1
        elif op == 2:
            return 2
        elif op == 3:
            return 3
        elif op == 4:
            return 4
        elif op == 5:
            return 5
        else:
            print("Opção Inválida")
            op = int(input("Digite a opção desejada:"))
    print("\nEncerrando programa...\n")
    return 0

def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num-1)

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 3:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)   

def soma(v,k):
    if k == 0:
        return v[k]
    else:
        return soma(v,k-1) + v[k]

def potencia(x,n):
    if n == 0:
        return 1
    else:
        return x * potencia(x,n-1)

def MDC(x,y):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return MDC(y,x)
    else:
        return MDC(y,x % y)

def main():
    opcao = menu()
    while opcao != 0:
        if opcao == 1:
            num = int(input("Digite um valor para ver o fatorial:"))
            if num < 0:
                print("Não existe fatorial de número negativo!")
            else:
                print(f"Fatorial de {num} é",fatorial(num))
        elif opcao == 2:
            num = int(input("Digite uma número/posição para ver o valor dele na sequência de fibonacci:"))
            if num < 0:
                print("Não existe fibonacci de número negativo!")
            else:
                print(f"Fibonacci da posição {num} é",fibonacci(num))
        elif opcao == 3:
            lista = [] #vetor
            n = int(input("Digite o tamanho da lista/vetor:"))
            if n >= 1:
                for i in range(n):
                    num = int(input("Digite um valor para adicionar na lista/vetor:"))
                    lista.append(num)
                print(f"Soma dos valores da lista/vetor é",soma(lista,n-1))
            else:
                print("Tamanho de lista/vetor Inválido!")
        elif opcao == 4:
            base = int(input("Digite o valor da base:"))
            expoente = int(input("Digite o valor do expoente:"))
            if expoente == 0 and base == 0:
                print("Valor Indefinido")
            else:
                print(f"{base} elevado a {expoente} é",potencia(base,expoente))
        else:
            print("Digite dois valores para calcular o MDC")
            x = int(input("Primeiro valor:"))
            y = int(input("Segundo valor:"))
            print(f"MDC de {x} e {y} é",MDC(x,y))
        opcao = menu()
main()