def somar_elementos(lista):
    i = 0
    soma = 0
    while i < len(lista):
        soma += lista[i]
        i += 1
    return soma

def main():
    i = 0
    L = []
    tam = int(input("Digite o tamanho da lista:"))
    while i < tam:
        num = float(input("Digite uma valor para adicionar na lista:"))
        L.append(num)
        i += 1
    print("Soma dos elementos da lista:",somar_elementos(L))

main()
