#exercicio 6 aula 8
def criar_matriz(matriz,n,m,nome):
    i = 0
    while i < n:
        print(f"Digite os elementos da linha {i} da matriz {nome}:")
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

def criar_matriz_C(A,B,col_A,lin_B,lin_A,col_B):
    C = []
    if col_A == lin_B:
        i = 0
        while i < lin_A:
            linha_c = []
            j = 0
            while j < col_B:
                soma = 0
                t = 0
                while t < col_A:
                    soma += A[i][t] * B[t][j]
                    t += 1
                linha_c.append(soma)
                j += 1
            C.append(linha_c)
            i += 1
        return C

def main():
    nome_A = "A"
    nome_B = "B"
    A = []
    lin_A = int(input("Informe o número de linhas que deseja para matriz A:"))
    col_A = int(input("Informe o número de colunas que deseja para matriz A:"))
    B = []
    lin_B = int(input("Informe o número de linhas que deseja para matriz B:"))
    col_B = int(input("Informe o número de colunas que deseja para matriz B:"))
    criar_matriz(A,lin_A,col_A,nome_A)
    criar_matriz(B,lin_B,col_B,nome_B)
    print("\n")
    print("Imprimindo a matriz A...")
    imprimir_matriz(A)
    print("\n")
    print("Imprimindo a matriz B...")
    imprimir_matriz(B)
    C = criar_matriz_C(A,B,col_A,lin_B,lin_A,col_B)
    print("\n")
    print("Imprimindo a matriz C...")
    if col_A == lin_B:
        imprimir_matriz(C)
    else:
        print("Não é possível imprimir C, pois não é possível realizar o produto das matrizes A e B")



main()