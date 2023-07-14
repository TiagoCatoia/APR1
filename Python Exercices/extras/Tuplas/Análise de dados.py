#usou count e index
num = (int(input("Digite o primero número:")),
       int(input("Digite o segundo número:")),
       int(input("Digite o terceiro número:")),
       int(input("Digite o quarto número:")),
)

print(f"O número 9 apareceu {num.count(9)} vezes")

achou_3 = False
for i in num:
    if i == 3 and achou_3 == False:
        achou_3 = True
        print(f"O primero número 3 foi digitado na posição {num.index(3)+1}")
if achou_3 == False:
    print("O número 3 não foi digitado nenhuma vez")

contador = 0
print("Números pares digitados:")
for i in num:
    if i % 2 == 0:
        print(f"{i} | ",end="")
        contador += 1
print()
if contador != 0:
    print(f"Foram digitados {contador} números pares")
else:
    print("Não foram digitados números pares")