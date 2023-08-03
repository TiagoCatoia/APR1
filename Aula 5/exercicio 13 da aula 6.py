def uniao_listas(lista1,lista2):
    L3 = lista1 + lista2
    return L3

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
    saida = input("Escolha o modo de saída(U:união, I:intersecção, D:diferença):")
    while saida != "U" and saida != "I" and saida != "D":
        print("Tente novamente!!!")
        saida = input("Escolha o modo de saída U,I ou D:")
    if saida == "U":
        print("Lista União:",uniao_listas(L1,L2))
    if saida == "I":
        print("Lista Intersecção:",interseccao_listas(L1,L2,tam1,tam2))
    if saida == "D":
        print("Lista Diferença:",diferenca_listas(L1,L2))
        
#######################################################################################################

main()
