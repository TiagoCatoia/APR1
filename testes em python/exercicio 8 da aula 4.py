n = int(input("Digite um número para ver o fatorial:"))

while n < 0:
    n = int(input("Digite um número positivo para ver o fatorial:"))

fatorial = 1
y = 1
while y <= n:
    fatorial = fatorial * y
    y = y + 1
print("O fatorial de",n,"é",fatorial)
