
def criar_matriz(matriz,n,m):
    i = 0
    while i < n:
        print(f"Entre com os elementos da linha {i} da matriz")
        linha = []
        j = 0
        while j < m:
            elemento = int(input())
            linha.append(elemento)
            j += 1
        matriz.append(linha)
        i += 1

def criar_matriz_C(A,lin_A,col_A,B,lin_B,col_B):
    C = []
    i = 0
    while i < lin_A:
        linha = []
        t = 0
        while t < col_B:
            soma = 0
            j = 0
            while j < col_A:
                soma += A[i][j] * B[j][t]
                j += 1
            linha.append(soma)
            t += 1
        C.append(linha)
        i += 1
    return C

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

def main():
    A = []
    lin_A = int(input("Digite o número de linhas da matriz A:"))
    col_A = int(input("Digite o número de colunas da matriz A:"))
    criar_matriz(A,lin_A,col_A)
    B = []
    lin_B = int(input("Digite o número de linhas da matriz B:"))
    col_B = int(input("Digite o número de colunas da matriz B:"))
    criar_matriz(B,lin_B,col_B)
    C = criar_matriz_C(A,lin_A,col_A,B,lin_B,col_B)
    if col_A == lin_B:
        imprimir_matriz(C)
    else:
        print("Não é possível imprimir C, pois não é possível realizar o produto das matrizes A e B")


main()