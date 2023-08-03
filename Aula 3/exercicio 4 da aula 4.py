#com for
n = int(input("Digite um número: "))
if n <= 1:
    print("Não é primo")
else:
    resto = 1
    for t in range(2, n):
        resto = resto * (n % t)
    if resto != 0:
        print("É primo")
    else:
        print("Não é primo")

#com while
n = int(input("Digite um número: "))
if n <= 1:
    print("Não é primo")
else:
    t = 2
    resto = 1
    while t < n:
        resto = resto * (n % t)
        t = t + 1
    if resto != 0:
        print("É primo")
    else:
        print("Não é primo")
