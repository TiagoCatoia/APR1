#exercicio 4 da aula 8
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

def verifica_identidade(matriz,dim):
    print("\n")
    identidade = True
    i = 0
    while i < len(matriz) and identidade == True:
        j = 0
        while j < len(matriz[i]) and identidade == True:
            if i == j:
                if matriz[i][j] != 1:
                    identidade = False
            else:
                if matriz[i][j] != 0:
                    identidade = False
            j += 1
        i += 1
    if identidade:
        print("A matriz é identidade")
    else:
        print("A matriz não é identidade")


def imprimir_matriz(matriz):
    print("\n")
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
    imprimir_matriz(Matriz)
    verifica_identidade(Matriz,dim)

main()