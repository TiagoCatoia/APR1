def aumentar(preco, taxa, formato = False): ##se não informar o formato será False
    res = preco + (preco * taxa/100)
    return res if formato == False else moeda(res)


def diminuir(preco, taxa, formato = False):
    res = preco - (preco * taxa/100)
    return res if formato == False else moeda(res)

def dobro(preco, formato = False):
    res = preco * 2
    return res if formato == False else moeda(res)

def metade(preco, formato = False):
    res =  preco / 2
    return res if formato == False else moeda(res)

def moeda(preco = 0): #se não informar o preço ele sera = 0
    res = f"R${preco:.2f}".replace(".",",")
    return res

def resumo(preco = 0, taxa1 = 10, taxa2 = 5):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"Preço aumentado em {taxa1}%: {aumentar(preco, taxa1, True)}")
    print(f"Preço diminuido em {taxa2}%: {diminuir(preco, taxa2, True)}")
    print("-"*30)
