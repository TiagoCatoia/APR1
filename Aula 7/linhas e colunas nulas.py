#exericicio 5 da aula 8
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

def zeros(matriz,n,m):
    contador_linha = 0
    i = 0
    while i < n: # verifica as linhas
        zero = True
        j = 0
        while j < m:
            if matriz[i][j] != 0:
                zero = False
            j += 1
        if zero == True:
            contador_linha += 1
        i += 1
    contador_coluna = 0
    j = 0
    while j < m: # verifica as colunas
        zero = True
        i = 0
        while i < n:
            if matriz[i][j] != 0:
                zero = False
            i += 1
        if zero == True:
            contador_coluna += 1
        j += 1
    print("\n")
    print("Quantidade de linhas nulas:",contador_linha)
    print("Quantidade de colunas nulas:",contador_coluna)




def main():
    Matriz = []
    lin = int(input("Informe o número de linhas que deseja para matriz:"))
    col = int(input("Informe o número de colunas que deseja para matriz:"))
    criar_matriz(Matriz,lin,col)
    print("\n")
    print("Imprimindo a matriz...")
    imprimir_matriz(Matriz)
    zeros(Matriz,lin,col)


main()