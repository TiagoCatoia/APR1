def inteiro(n,verificador):
    if n == verificador:
        return "Verdadeiro"
    else:
        return"False"

def main():
    num = float(input("Digite um número para verifica se é inteiro:"))
    verificador = int(num)
    print(inteiro(num,verificador))

main()
