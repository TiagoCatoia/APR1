a = float(input("Digite o valor a:"))
b = float(input("Digite o valor b:"))
c = float(input("Digite o valor c:"))
if a == 0:
    delta = 0
    print("A incognita 'a' deve ser diferente de 0 para termos uma eq. do 2° grau")
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Não existe solução real")
    elif delta == 0:
        x = (-b)/(2*a)
        print(x)
    else:
        x1 = (-b - delta**(1/2)) /(2*a)
        x2 = (-b + delta**(1/2)) /(2*a)
        print("Valor das raízes:",x1,x2)

