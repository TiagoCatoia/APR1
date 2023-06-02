str = input("Digite uma string:")
letra_remover = input("Digite uma letra para remover:")
str = str.replace(letra_remover,"")
print(str)


#OU SEM USAR REPLACE


str1 = input("Digite uma string:")
letra_remover = input("Digite uma letra para remover:")
i = 0
str2 = ""
while i < len(str1):
    if letra_remover not in str1[i]:
        str2 += str1[i]
    i += 1
print(str2)


