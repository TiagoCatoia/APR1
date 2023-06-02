frase = input("Digite uma frase:")
while " " not in frase:
    print(f"'{frase}' Não é uma frase, tente novamente!")
    frase = input("Digite uma frase:")

vogais = "aeiou"
contador_vogais = 0
contador_espaco = 0
i = 0
while i < len(frase):
    if frase[i] in vogais:
        contador_vogais += 1
    if frase[i] in " ":
        contador_espaco += 1
    i += 1
print("Quantidade de espaços em branco:",contador_espaco)
print("Quantidade de vezes que aparecem as vogais a, e, i, o, u:",contador_vogais)