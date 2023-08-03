str = input("Digite uma string:")
letra_remover = input("Digite uma letra para remover:")
str = str.replace(letra_remover,"",1)
print(str)

#OU SEM USAR REPLACE

str1 = input("Digite uma string:")
letra_removr = input("Digite uma letra para remover:")
i = 0
str2 = ""
replace = False
while i < len(str1):
    if letra_remover in str1[i] and replace == False:
        replace = True
    else:
        str2 += str1[i]
    i += 1
print(str2)