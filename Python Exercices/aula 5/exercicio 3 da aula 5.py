#JUNTO
n = int(input("Digite quantos números deseja adicionar:"))
#JUNTO
sequencia = []
soma = 0
multi = 1
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    if num % 2 == 0:
        soma += num
    else:
        multi *= num
    sequencia.append(num)
    i += 1
print("Valores da sequência:",sequencia)
print("Soma dos pares da sequência:",soma)
print("Produto dos valores ímpares da sequência:",multi)

#SEPARADO
n = int(input("Digite quantos números deseja adicionar:"))
sequencia = []
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    sequencia.append(num)
    i += 1
print("Valores da sequência:",sequencia)

i = 0
soma = 0
multi = 1
while i < len(sequencia):
    if sequencia[i] % 2 == 0:
        soma += sequencia[i]
    else:
        multi *= sequencia[i]
    i += 1
print("Soma dos valores pares da sequência:",soma)
print("Produto dos valores ímpares da sequência:",multi)


