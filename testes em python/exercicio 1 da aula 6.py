def inteiro_positivo(n,inteiro):
    if n > 0 and n == inteiro:
        return "Verdadeiro"
    else:
        return "Falso"

def main():
    num = float(input("Digite um número para verifica se é inteiro e positivo:"))
    inteiro = int(num)
    print(inteiro_positivo(num,inteiro))

main()
