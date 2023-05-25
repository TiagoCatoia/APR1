n = int(input("Digite uma nota(negativo para sair):"))
i = 0
lista = []
soma = 0
contador = 0
while n >= 0:
    soma += n
    contador += 1
    lista.append(n)
    n = int(input("Digite uma nota(negativo para sair):"))
print("Sequência de notas:",lista)
print("Média das notas:",soma/contador)
