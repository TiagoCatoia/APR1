#exericicio 1 da aula 8
def criar_matriz(matriz,n,m):
    i = 0
    while i < n:
        print(f"Digite os elementos da linha {i}")
        j = 0
        linha = [] # guarda os elementos da linha i
        while j < m:
            elemento = int(input())
            linha.append(elemento)
            j += 1
        matriz.append(linha)
        i += 1

def imprimir_matriz(matriz):
    i = 0
    while i < len(matriz):
        print()
        print(f"Elementos da linha {i} ")
        j = 0
        while j < len(matriz[i]):
            print(f"{matriz[i][j]}", end=" ")
            j += 1
        i += 1

def maior_menor(matriz,m):
    i = 0
    j = 0
    maior = matriz[i][j]
    menor = matriz[i][j]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
            if matriz[i][j] < menor:
                menor = matriz[i][j]
    print("\n")
    print("Maior valor da matriz:",maior)
    print("Menor valor da matriz:",menor)


def main():
    Matriz = []
    lin = int(input("Informe o número de linhas que deseja para matriz:"))
    col = int(input("Informe o número de colunas que deseja para matriz:"))
    criar_matriz(Matriz,lin,col)
    print("\n")
    print("Imprimindo a matriz...")
    imprimir_matriz(Matriz)
    maior_menor(Matriz,col)


main()