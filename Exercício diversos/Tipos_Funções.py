#Função Modificadora(altera os elementos da lista)
def double_stuff(lista):
    i = 0
    while i < len(lista):
        lista[i] = 2 * lista[i]
        i += 1
#Função Pura(NÂO altera os elementos da lista)
def double_stuff2(lista):
    i = 0
    while i < len(lista):
        L4.append(2 * lista[i])
        i += 1
    


things=[2,5,9]
print(things)
double_stuff(things)
print(things)
L4 = []
double_stuff2(things)
print(L4)


#OU COM RETURN

#Função Modificadora(altera os elementos da lista)
def double_stuff(lista):
    i = 0
    while i < len(lista):
        lista[i] = 2 * lista[i]
        i += 1
#Função Pura(NÂO altera os elementos da lista)
def double_stuff2(lista):
    i = 0
    dobro = []
    while i < len(lista):
        dobro.append(2 * things[i])
        i += 1
    return dobro


things=[2,5,9]
print(things)
double_stuff(things)
print(things)
L4 = double_stuff2(things)
print(L4)
