num = input("Digite um número inteiro:")
verifica_se_str = True
while verifica_se_str == True:
    try:
        int(num)
        verifica_se_str = False   #string não pode ser convertida em inteiro logo quando for False é porque é um número inteiro
    except:
        print(f"{num} Não é um inteiro tente novamente!")
        num = input("Digite um número inteiro:")
if int(num) < 0:
    print(len(num)-1)
else:
    print(len(num))