#exercicio 3 da aula 8
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

def criar_transposta(matriz,n,m,transposta):
    for j in range(m):
        linha = []
        for i in range(n):
            linha.append(matriz[i][j])
        transposta.append(linha)

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
    Matriz = []
    Transposta = []
    lin = int(input("Informe o número de linhas que deseja para matriz:"))
    col = int(input("Informe o número de colunas que deseja para matriz:"))
    criar_matriz(Matriz,lin,col)
    print("\n")
    print("Imprimindo a matriz...")
    imprimir_matriz(Matriz)
    print("\n")
    print("Imprimindo a sua transposta...")
    criar_transposta(Matriz,lin,col,Transposta)
    imprimir_matriz(Transposta)

main()
