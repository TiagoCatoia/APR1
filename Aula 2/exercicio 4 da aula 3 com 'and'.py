a = int(input("Valor de a:"))
b = int(input("Valor de b:"))
c = int(input("Valor de c:"))
if a + b > c and a + c > b and b + c > a:
    print("É possível formar um triangulo com esses valores")
    if a == b == c:
        print("Triângulo equilátero")
    elif a == b and a != c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Com esses valores não é possível formar um tringulo")
