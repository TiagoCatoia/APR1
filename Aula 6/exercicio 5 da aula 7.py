frase = input("Digite uma frase:")
while " " not in frase:
    print(f"'{frase}' Não é uma frase, tente novamente!")
    frase = input("Digite uma frase:")

frase = frase.replace(" ","")
print("Número de palavras que a frase contém:",len(frase))
