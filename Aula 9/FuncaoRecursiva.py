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
    lista = []
    i = 0
    n = int(input("Digite o tamanho da lista:"))
    while i < n:
        elemento = int(input("Entre com um valor para adicionar na lista:"))
        lista.append(elemento)
        i += 1
    print("Soma dos elementos da lista:",soma(lista,n-1))

    x = int(input("Digite a base de uma potência:"))
    n = int(input("Digite o expoente de uma potência:"))
    print(f"Potência de {x} elevado a {n}:",potencia(x,n))

    print("Digite dois valores para calcular o MDC")
    x = int(input("Primeiro valor:"))
    y = int(input("Segundo valor:"))
    print(f"MDC de {x} e {y} é",MDC(x,y))
    
main()