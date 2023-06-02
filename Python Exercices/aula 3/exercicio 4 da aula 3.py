a = int(input("Valor de A:"))
b = int(input("Valor de B:"))
c = int(input("Valor de C:"))
if a + b > c:
    if a + c > b:
        if b + c > a:
            print("É possível formar um triangulo com estes valores")
        else:
            print("Com esses valores não é possível formar um tringulo")
    else:
        print("Com esses valores não é possível formar um tringulo")
else:
    print("Com esses valores não é possível formar um tringulo")


if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b == c:
                print("Triângulo equilátero")
            elif a == b and a != c:
                print("Triângulo isósceles")
            else:
                print("Triângulo escaleno")
