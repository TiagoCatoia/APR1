n = int(input("Digite quantos números deseja adicionar:"))
sequencia1 = []
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    sequencia1.append(num)
    i += 1
print("Primeira sequência:",sequencia1)

sequencia2 = []
i = 0
while i < n:
    num = int(input("Entre com um número:"))
    sequencia2.append(num)
    i += 1
print("Segunda sequência:",sequencia2)

somatoria = []
i = 0
while i < n:
    soma = sequencia1[i] + sequencia2[i]
    somatoria.append(soma)
    i += 1
print("Soma das sequencias:",somatoria)


#ABAIXO UMA OPÇÂO CASO O QUANTIA DE ELEMENTOS NAS LISTAS FOSSEM DIFERENTES

if len(sequencia1) >= len(sequencia2):  #É possível usar max com 1 while e sem if
    while i < len(sequencia1):          #while i < max(len(sequencia1),len(sequencia2))
        soma = (sequencia1[i]) + (sequencia2[i] if i < len(sequencia2) else 0)
        somatoria.append(soma)
        i += 1
else:
    while i < len(sequencia2):
        soma = (sequencia1[i] if i < len(sequencia1) else 0) + (sequencia2[i])
        somatoria.append(soma)
        i += 1
