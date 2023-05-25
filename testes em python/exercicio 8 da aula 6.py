def inteiro_positivo(n,inteiro):
    while n <= 0 or n != inteiro: #verifica se o não é positivo ou inteiro
        print(f"{n} Não é um número de termos aceitável, tente um inteiro positivo!")
        num2 = float(input("Digite quantos termos da sequência de Fibonacci deseja ver:"))
        inteiro = int(num2)
        n = num2
    return True


def main():
    num = float(input("Digite quantos termos da sequência de Fibonacci deseja ver:"))
    inteiro = int(num)
    if inteiro_positivo(num,inteiro):
        a = "Verdade"
        i = 0
        antecessor = 0
        proximo = 1
        while i < num:
            print(antecessor, end=" ")
            soma = antecessor + proximo
            antecessor = proximo
            proximo = soma
            i += 1


main()
