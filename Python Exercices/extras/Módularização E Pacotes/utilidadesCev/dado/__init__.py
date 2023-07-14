def leiaDinheiro(mensagem): #funciona como um input com um verificador
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(",",".").strip() #strip tira os espaços vazios
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m")
        else:
            valido = True
            return float(entrada)