def interseccao_listas(lista1,lista2,tam1,tam2):
    i = 0
    L3 = []
    while i < tam1:
        t = 0
        while t < tam2:
            if lista1[i] == lista2[t]:
                L3.append(lista1[i])
            t += 1
        i += 1
    return L3


def main():
    i = 0
    L1 = []
    L2 = []
    print("Primeira lista")
    tam1 = int(input("Digite o tamanho da primeira lista:"))
    while i < tam1:
        num = int(input("Entre com um valor para adicionar na primeira lista:"))
        L1.append(num)
        i += 1
    print("Segunda lista")
    tam2 = int(input("Digite o tamanho da segunda lista:"))
    i = 0
    while i < tam2:
        num = int(input("Entre com um valor para adicionar na segunda lista:"))
        L2.append(num)
        i += 1
    print("Lista Intersecção:",interseccao_listas(L1,L2,tam1,tam2))

main()
    

    
