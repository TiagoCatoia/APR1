def uniao_listas(lista1,lista2):
    L3 = lista1 + lista2
    return L3


def main():
    i = 0
    L1 = []
    L2 = []
    print("Primeira lista")
    tam1 = int(input("Digite o tamanho da primeira lista:"))
    while i < tam1:
        num = int(input("Entre com o valor para adicionar na primeira lista:"))
        L1.append(num)
        i += 1
    print("Segunda lista")
    tam2 = int(input("Digite o tamanho da segunda lista:"))
    i = 0
    while i < tam2:
        num = int(input("Entre com o valor para adicionar na segunda lista:"))
        L2.append(num)
        i += 1
    print("Lista União:",uniao_listas(L1,L2))

main()
    

    
