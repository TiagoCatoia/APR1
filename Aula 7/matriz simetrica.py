#exercicio 2 da aula 8
def criar_matriz(matriz,dimensao):
    i = 0
    while i < dimensao:
        print(f"Digite os elementos da linha {i}")
        j = 0
        linha = [] # guarda os elementos da linha i
        while j < dimensao:
            elemento = int(input())
            linha.append(elemento)
            j += 1
        matriz.append(linha)
        i += 1

def verifica_simetrica(matriz):
    simetrica = True
    i = 0
    while i < len(matriz) and simetrica == True:
        j = 0
        while j < len(matriz[i]) and simetrica == True:
            if matriz[i][j] != matriz[j][i]:
                simetrica = False
            j += 1
        i += 1
    print("\n")
    if simetrica:
        print("Está matriz é simetrica!")
    else:
        print("Está matriz não é simetrica!")

def imprimir_matriz(matriz):
    print("Imprimindo a matriz...")
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
    dim = int(input("Informe a dimensão da matriz quadrada:"))
    criar_matriz(Matriz,dim)
    verifica_simetrica(Matriz)
    imprimir_matriz(Matriz)


main()