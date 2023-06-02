#com for
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1
for y in range(expoente):
    resultado *= base

print(base,"elevado a",expoente,"é igual a",resultado)


#com while
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1
y = 0              #y é o meu contador de loops
while y < expoente:
    resultado = resultado * base
    y = y + 1
    
print(base,"elevado a",expoente,"é igual a",resultado)
