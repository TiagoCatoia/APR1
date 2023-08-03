def inteiro_positivo(n,inteiro):
    while n <= 0 or n != inteiro:  #verifica se n não é positivo ou inteiro
        print(f"{n} Não é um número intero positivo")
        num2 = float(input("Digite um número inteiro e positivo para ver o fatorial:"))
        inteiro = int(num2)
        n = num2
    i = 1
    fatorial = 1
    while i <= n:
        fatorial *=  i
        i += 1
    return fatorial

def main():
    num = float(input("Digite um número inteiro e positivo para ver o fatorial:"))
    inteiro = int(num)
    print(inteiro_positivo(num,inteiro))

main()
