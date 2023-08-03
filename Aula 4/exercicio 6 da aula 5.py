n = int(input("Digite quantos números deseja adicionar:"))
sequencia = []
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    sequencia.append(num)
    i += 1
print("Sequência original:",sequencia)

i = 0
cubo_da_sequencia = []
while i < len(sequencia):
    cubo_da_sequencia.append((sequencia[i])**3)
    i += 1
print("Sequência elevada ao cubo:",cubo_da_sequencia)
