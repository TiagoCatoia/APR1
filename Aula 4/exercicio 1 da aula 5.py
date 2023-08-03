i = 3
lista = [1]
while i <= 150:
    if i % 3 == 0:
        lista.append(i)
    i += 3
print("Lista com múltiplos de 3 entre 1 e 150:",lista)

#ou com list(range)
lista = list(range(3,153,3))
lista.insert(0,1)
print("Lista com múltiplos de 3 entre 1 e 150:",lista)
