def inteiro(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def main():
    num = int(input("Digite um valor:"))
    print(inteiro(num))

main()

    


