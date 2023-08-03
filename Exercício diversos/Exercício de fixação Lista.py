i = 0
L = []
soma = 0
while i < 10:
    num = int(input("Digite um valor:"))
    soma += num
    L.append(num)
    i += 1
print("Lista:",L)

i = 1
maior = L[0]
menor = L[0]
while i < len(L):
    if L[i] >= maior:
        maior = L[i]
    if L[i] <= menor:
        menor = L[i]
    i += 1
print("Maior elemento da lista:",maior)
print("Menor elemento da lista:",menor)
print("Soma dos elementos da lista:",soma)
print("Elementos ímpares:")
i = 0
while i < len(L):
    if L[i] % 2 != 0:
        print(L[i],end=" ") #impares
    i += 1
print("")
print("Elementos maiores que 18:")
i = 0
while i < len(L):
    if L[i] > 18:
        print(L[i],end=" ") #maiores que 18
    i += 1
