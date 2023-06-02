def anagrama(strg1,strg2):
    if len(strg1) != len(strg2):
        return "Falso"
    else:
        i = 0
        while i < len(strg1): #Percorre cada letra da string1
            letra = strg1[i]
            if letra in strg2:  #Verifica se a letra está presente na string2
                strg2 = strg2.replace(letra,"",1) #Remove a letra da string2
            i += 1
        if strg2 == "":
            return "Verdadeiro"
        else:
            return "False"


def main():
    strg1 = input("Digite a primeira string: ")
    strg2 = input("Digite a segunda string: ")

    strg1 = strg1.replace(" ","")
    strg2 = strg2.replace(" ","")
    print("Verdadeiro se forem um anagrama ou Falso se não forem:")
    print(anagrama(strg1,strg2))

        
main()




# OU USANDO FOR


def anagrama(strg1,strg2):
    if len(strg1) != len(strg2):
        return "Falso"
    else:
        for letra in strg1:
            if letra in strg2:  #Verifica se a letra está presente na string2
                strg2 = strg2.replace(letra,"",1) #Remove a letra da string2
        if strg2 == "":
            return "Verdadeiro"
        else:
            return "False"


def main():
    strg1 = input("Digite a primeira string: ")
    strg2 = input("Digite a segunda string: ")

    strg1 = strg1.replace(" ","")
    strg2 = strg2.replace(" ","")
    print("Verdadeiro se forem um anagrama ou Falso se não forem:")
    print(anagrama(strg1,strg2))

main()
