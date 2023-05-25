str1 = input("Digite a primeira string:")
str2 = input("Digite a segunda string:")
str1 = str1.lower()
str2 = str2.lower()

str1_nova = ""
str2_nova = ""

i = 0
while i < len(str1):
    if " " not in str1[i]:
        str1_nova += str1[i]
    i += 1
i = 0
while i < len(str2):
    if " " not in str2[i]:
        str2_nova += str2[i]
    i += 1

str2 = ""
if len(str1_nova) != len(str2_nova):
    print("Não é um anagrama!")
else:
    i = 0
    while i < len(str1_nova):
        letra = str1_nova[i]
        t = 0
        replace = False
        while t < len(str2_nova):
            if letra == str2_nova[t] and replace == False:
                replace = True
            else:
                str2 += str2_nova[t]

            t += 1
        i += 1
    
    if str2 == "":
        print("É um anagrama!")
    else:
        print(str2)
        print("Não é um anagrama!")


#verificar se letra esta em cada indice da outra string e se tiver remover e acabar o loop para não remover mais de uma



#OU COM REPLACE

str1 = input("Digite a primeira string:")
str2 = input("Digite a segunda string:")

str1 = str1.lower()
str2 = str2.lower()

str1 = str1.replace(" ","")
str2 = str2.replace(" ","")

if len(str1) != len(str2):
    print("Não é um anagrama!")
else:
    i = 0
    while i < len(str1):
        letra = str1[i]
        if letra in str2:
            str2 = str2.replace(letra,"")
        i += 1
    if str2 == "":
        print("É um anagrama!")
    else:
        print("Não é um anagrama!")
