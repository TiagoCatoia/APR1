def par_ate(n):
    print("Lista Pares:")
    lista_pares = []
    for i in range(2,n):
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares
            
def main():
    num = int(input("Digite até que número deseja ver os pares:"))
    pares = par_ate(num)
    print(pares)
################PRINCIPAL########################################
main()


#UMA OUTRA MANEIRA

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False
def par_ate(n):
    print("Lista Pares:")
    lista_pares = [num for num in range(2,n) if par(num)]
    return lista_pares

n = int(input("Digite até que número deseja ver os pares:"))
pares = par_ate(n)
print(pares)
