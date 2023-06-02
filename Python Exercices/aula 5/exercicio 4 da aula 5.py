n = int(input("Digite quantos números deseja adicionar:"))
sequencia = []
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    sequencia.append(num)
    i += 1
print("Sequência original:",sequencia)

i = 0
sem_repit = []
com_repit = []
while i < len(sequencia):
    if sequencia[i] not in sem_repit:
        sem_repit.append(sequencia[i])
    else:
        com_repit.append(sequencia[i])
    i += 1
print("Elementos que não se repetem na sequência:",sem_repit)
print("Elementos que se repetem na sequência:",com_repit)

#OU sem in padrão outras linguagens fora python

n = int(input("Digite quantos números deseja adicionar:"))
sequencia = []
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    sequencia.append(num)
    i += 1
print("Sequência original:",sequencia)

i = 0
sem_repit = []
com_repit = []
while i < len(sequencia):
    if len(sem_repit) == 0:
        sem_repit.append(sequencia[i])
    else:
        achou = False
        j = 0
        while j < len(sem_repit) and achou == False:
            if sequencia[i] == sem_repit[j]:
                com_repit.append(sequencia[i])
                achou = True
            j += 1
        if achou == False:
            sem_repit.append(sequencia[i])
    i += 1

print("Elementos que não se repetem na sequência:",sem_repit)
print("Elementos que se repetem na sequência:",com_repit)

