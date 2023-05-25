n = int(input("Digite quantos números deseja adicionar:"))
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    sequencia.append(num)
print("Sequência original:",sequencia)

i = len(sequencia) - 1 
sequencia_invertida = []
while i >= 0:
    sequencia_invertida.append(sequencia[i])
    i -= 1
print("Sequência invertida:",sequencia_invertida)

#OU

n = int(input("Digite quantos números deseja adicionar:"))
sequencia = []
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    sequencia.append(num)
    i += 1
print("Sequência original:",sequencia)

i = - 1 
sequencia_invertida = []
while i >= -len(sequencia):
    sequencia_invertida.append(sequencia[i])
    i -= 1
print("Sequência invertida:",sequencia_invertida)
    
