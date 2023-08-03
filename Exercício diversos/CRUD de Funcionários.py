class Funcionario:
    cpf = -1
    nome = ""
    idade = -1
    salario = -1

def menu_opcoes():
    print("\n")
    print("Menu de opções:")
    print("1. Cadastrar funcionário")
    print("2. Consultar dados de um funcionário")
    print("3. Consultar dados de todos os funcionários")
    print("4. Remover funcionário")
    print("5. Alterar dados de um funcionário")
    print("0. Sair")
    op = input("Escolha uma das opções:")
    print("\n")
    return op

def verifica_cpf(lista_func,cpf):
    for i in range(len(lista_func)):
        if lista_func[i].cpf == cpf:
            return i
    return -1

def cadastrar(lista_func):
    func = Funcionario()
    func.cpf = int(input("Entre com o CPF do funcionário que quer cadastrar:"))
    achou = verifica_cpf(lista_func,func.cpf)
    if achou == -1:
        func.nome = input("Entre com o nome completo do funcionário:")
        func.idade = int(input("Entre com a idade do funcionário:"))
        func.salario = int(input("Entre com o salário do funcionário:"))
        lista_func.append(func)
        print("\n")
    else:
        print("Este CPF já está cadastrado!")

def consultar(lista_func,cpf):
    Cadastrado = False
    i = 0
    while i < len(lista_func) and Cadastrado == False:
        if lista_func[i].cpf == cpf:
            print("Nome:",lista_func[i].nome,"Idade:",lista_func[i].idade,"Salário: "+"R$"+str(lista_func[i].salario)+",00","CPF:",str(lista_func[i].cpf))
            Cadastrado = True
        i += 1
    if Cadastrado == False:
        print("Este funcionário não está cadastrado!")

def consultar_todos(lista_func):
    for i in range(len(lista_func)):
        print("Nome:",lista_func[i].nome,"Idade:",lista_func[i].idade,"Salário: "+"R$"+str(lista_func[i].salario)+",00","CPF:",str(lista_func[i].cpf))

def remover_func(lista_func):
    cpf = int(input("Digite o CPF do funcionário que deseja remover:"))
    posicao = verifica_cpf(lista_func,cpf)
    if posicao != -1:
        del lista_func[posicao]
        print("\n")
        print("Funcionário removido com sucesso!")
    else:
        print("\n")
        print("Falha na remoção, este funcionário não está cadastrado!")

def opcoes_alterar():
    print("\n")
    print("1. Alterar o nome do funcionário")
    print("2. Alterar a idade do funcionário")
    print("3. Alterar o salário do funcionário")
    print("4. Alterar o cpf do funcionário")
    print("5. Alterar todos os dados do funcionário")
    op = input("Escolha uma das opções:")
    print("\n")
    return op

def alterar_func(lista_func):
    cpf = int(input("Digite o CPF do funcionário que deseja alterar dados:"))
    posicao = verifica_cpf(lista_func,cpf)
    if posicao != -1:
        op = opcoes_alterar()
        if op == "1":
            lista_func[posicao].nome = input("Entre com o nome completo do funcionário:")
        elif op == "2":
            lista_func[posicao].idade = int(input("Entre com a idade do funcionário:"))
        elif op == "3":
            lista_func[posicao].salario = int(input("Entre com o salário do funcionário:"))
        elif op == "4":
            print("Não é possível alterar o CPF de um funcionário, tente removê-lo e cadastra-lo novamente!")
        elif op == "5":
            lista_func[posicao].nome = input("Entre com o nome completo do funcionário:")
            lista_func[posicao].idade = int(input("Entre com a idade do funcionário:"))
            lista_func[posicao].salario = int(input("Entre com o salário do funcionário:"))
        else:
            print("Opção Inválida!")
    else:
        print("\n")
        print("Falha na alteração, este funcionário não está cadastrado!")

def main():
    funcionarios = []
    i = 0
    opcao = menu_opcoes()
    while opcao != "0":
        if opcao == "1":
            cadastrar(funcionarios)
        elif opcao == "2":
            cpf_func = int(input("Digite o CPF do funcionário que deseja consultar os dados:"))
            print("\n")
            consultar(funcionarios,cpf_func)
        elif opcao == "3":
            consultar_todos(funcionarios)
        elif opcao == "4":
            remover_func(funcionarios)
        elif opcao == "5":
            alterar_func(funcionarios)
        else:
            print("Opção Inválida!")
        opcao = menu_opcoes()

main()
