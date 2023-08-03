produtos = ("Lápis",1.50,
            "Borracha",2.50,
            "Apontador",4.25,
            "Mochila",150,
            "Estojo",15,
            "Caneta",2,
            "Régua",8.50,
            "Compasso",10.25,
)
print("LISTA DE PREÇOS:")

for i in range(0,len(produtos)):
    if i % 2 == 0:
        print(f"{produtos[i]:.<30}",end="") #material
    else:
        print(f"R${produtos[i]:>7.2f}") #preço