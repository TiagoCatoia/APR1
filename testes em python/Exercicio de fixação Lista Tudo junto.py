lista = []
i = 0
y = 2
num = int(input("Digite um valor para por na lista:"))
maior = num
menor = num
soma = 0
impares = []
maior_dezoito = []
while i < 9:
    if num % 2 != 0:
        impares.append(num)
    if num > 18:
        maior_dezoito.append(num)
    soma += num
    lista.append(num)
    num = int(input("Digite um valor para por na lista:"))
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    i += 1
print("Lista:",lista)
print("Maior numero da lista:",maior)
print("Menor numero da lista:",menor)
print("Soma dos elementos da lista:",soma)
print("Números ímpares:",impares)
print("Númeors maiores que dezoito:",maior_dezoito)

