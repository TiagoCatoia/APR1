num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))
if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    maior = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    maior = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    maior = num3
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    maior = num4
else:
    maior = num5
print("O maior número é:",maior)







