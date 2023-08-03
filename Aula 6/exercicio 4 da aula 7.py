str = input("Digite uma string: ")
str_nova = str[::-1]  # Inverte a string utilizando slice
if str == str_nova:
    print("A string é um palíndromo!")
else:
    print("A string não é um palíndromo!")

#OU


str1 = input("Digite uma string: ")
i = -1
str2 = ""
while i >= -len(str1): # Inverte a string utilizando while
    str2 += str1[i]
    i -= 1
print(str2)
if str == str_nova:
    print("A string é um palíndromo!")
else:
    print("A string não é um palíndromo!")


#OU sem inverter a string


str = input("Digite uma string:")
i = 0
y = 1
t = -2
finalizar = False
if str[i] == str[-1]:
    while i < len(str) and finalizar == False:
        try:
            if str[y] == str[t]:
                y += 1
                t -= 1
            else:
                print("A string não é um palíndromo!")
                finalizar = True
        except:
            print("A string é um palíndromo!")
            finalizar = True
    i += 1

else:
    print("A string não é um palíndromo!")

    