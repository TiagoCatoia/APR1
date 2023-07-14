from datetime import datetime
dados = dict()
dados["nome"] = input("Nome: ")
nasc  = int(input("Ano de nascimento: "))
dados["idade"] = datetime.now().year - nasc
dados["ctps"] = int(input("Carteira de Trabalho (0 se não tem): "))
if dados["ctps"] != 0:
    dados["contatracao"] = int(input("Ano de Contratação: "))
    dados["salario"] = int(input(f"Salário em {dados['contatracao']}: "))
    dados["aposentadoria"] = dados["idade"] + ((dados["contatracao"] + 35) - datetime.now().year)
print("-=" * 30)
print(f" - Nome: {dados['nome']}")
print(f" - Idade: {dados['idade']}")
if dados['ctps'] == 0:
    print(f" - {dados['nome']} não possui Carteira de Trabalho")
else:
    print(f" - Carteira de Trabalho: {dados['ctps']}")
    print(f" - Salário no ano {dados['contatracao']}: R$ {dados['salario']:.2f}")
    print(f" - {dados['nome']} pode se aposentar a partir dos {dados['aposentadoria']} anos")