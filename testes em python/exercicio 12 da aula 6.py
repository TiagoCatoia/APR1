

def diferenca_listas(lista1,lista2):
    i = 0
    L3 = []
    if len(lista1) >= len(lista2):
        while i < len(lista1):
            t = 0
            diferenca1 = False
            diferenca2 = False
            while t < len(lista2):
                if lista1[i] not in lista2 and diferenca1 == False:
                    L3.append(lista1[i])
                    diferenca1 = True
                if i >= len(lista2):
                    diferenca2 = True
                else:
                    if lista2[i] not in lista1 and diferenca2 == False:
                        L3.append(lista2[i])
                        diferenca2 = True
                t += 1
            i += 1
    else:
        while i < len(lista2):
            t = 0
            diferenca1 = False
            diferenca2 = False
            while t < len(lista2):
                if lista2[i] not in lista1 and diferenca2 == False:
                    L3.append(lista2[i])
                    diferenca2 = True
                if i >= len(lista1):
                    diferenca2 = True
                else:
                    if lista1[i] not in lista2 and diferenca1 == False:
                        L3.append(lista1[i])
                        diferenca1 = True
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
    print("Lista Diferença:",diferenca_listas(L1,L2))

main()
