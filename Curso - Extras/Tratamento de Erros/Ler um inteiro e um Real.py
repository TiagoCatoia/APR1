def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print(f"\033[0;31mErro: por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            return (f"\033[0;31m\nO Usuário prefiriu não digitar o valor.\033[m")
        else:
            return num

def leiaReal(msg):
    while True:
        try:
            num = float(input(msg))
        except (TypeError, ValueError):
            print(f"\033[0;31mErro: por favor, digite um número real válido.\033[m")
            continue
        except KeyboardInterrupt:
            return (f"\033[0;31m\nO Usuário prefiriu não digitar o valor.\033[m")
        else:
            return num     


num = leiaInt("Digite um número inteiro:")
print(f"O valor inteiro digitado foi {num}")
print("\n")
num = leiaReal("Digite um número real:")
print(f"O valor real digitado foi {num}")