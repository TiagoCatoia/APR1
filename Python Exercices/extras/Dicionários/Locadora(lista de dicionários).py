#USANDO COPY
estado = dict() #estado = {}
brasil = list() #brasil = []
for c in range(0,3):
    estado["uf"] = str(input("Unidade Federativa:"))
    estado["sigla"] = str(input("Sigla do Estado:"))
    brasil.append(estado.copy())
for estado in brasil: #estado assume o valor de cada dicionário
    for v in estado.values():
        print(f"{v}",end=" ")
    print()

#ATRIBUINDO VALOR VAZIO PARA O DICIONARIO EM CADA LOOP

brasil = list() #brasil = []
for c in range(0,3):
    estado = dict() #estado = {}
    estado["uf"] = str(input("Unidade Federativa:"))
    estado["sigla"] = str(input("Sigla do Estado:"))
    brasil.append(estado)
for estado in brasil: #estado assume o valor de cada dicionário
    for v in estado.values():
        print(f"{v}",end=" ")
    print()