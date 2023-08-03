n = int(input("Digite quantos números deseja adicionar:"))
sequencia = []
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    sequencia.append(num)
    i += 1
print("Sequência original:",sequencia)

i = 0
sequencia_alterada = []
while i < len(sequencia):
    if sequencia[i] % 2 == 0:
        sequencia[i] = +1
    else:
        sequencia[i] = -1
    i += 1
print("Sequência alterada:",sequencia)
