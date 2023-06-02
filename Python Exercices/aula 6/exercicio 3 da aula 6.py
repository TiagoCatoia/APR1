def real(n):
    try:
        float(n)
        return "True"

    except:
        return "False"

def main():
    num = input("Digite um valor:")
    print(real(num))
    
main()
