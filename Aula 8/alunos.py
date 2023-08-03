class Aluno:
    nome = ""
    nota = ""

def menu_opcoes():
    print("\n")
    print("1.Cadastrar notas de um aluno")
    print("2.Imprimir notas de todos os alunos")
    print("3.Retornar o nome do estudante que possui mais de 6 notas")
    print("4.Vizualizar a média de aluno")
    print("5.Vizualizar a maior e a menor nota de um aluno")
    print("0.Sair")
    opcao = int(input("Escolha uma opção:"))
    return opcao

def verifica_aluno(lista_alunos,nome):
    for i in range(len(lista_alunos)):
        if lista_alunos[i].nome == nome:
            return i
    return -1

def cadastro_notas(lista_alunos):
    al = Aluno()
    print("Cadastrando notas...")
    al.nome = input("Entre com o nome completo do aluno:")
    achou = verifica_aluno(lista_alunos,al.nome)
    al.nota = []
    if achou == -1:
        nota = int(input("Entre com a nota:"))    # lembrar de criar um loop para qnd a nota for negativa!
        al.nota.append(nota)
        mais = int(input("Deseja cadastrar mais uma nota(1 para SIM):"))
        while mais == 1:
            nota = int(input("Entre com a nota:"))
            al.nota.append(nota)
            mais = int(input("Deseja cadastrar mais uma nota(1 para SIM):"))
        lista_alunos.append(al)
    else:
        print("\nEsse aluno já está cadastrado!")

def imprimir_alunos(lista_alunos):
    if len(lista_alunos) == 0:
        print("\nNão existem alunos cadastrados!")
    else:
        for i in range(len(lista_alunos)):
            print(f"Nome: {lista_alunos[i].nome} | Notas: {lista_alunos[i].nota}")

def nome_mais_6notas(lista_alunos): # retorna o nome do aluno que possui mais de 6 notas
    existe = False
    for i in range(len(lista_alunos)):
        if len(lista_alunos[i].nota) > 6:
            existe = True
            print("\nAnulo com nota maior que 6:")
            print(lista_alunos[i].nome)
    if existe == False:
        print("\nNão existem alunos com mais de 6 notas!")

def ver_media(lista_alunos):
    nome = input("\nDigite o nome do aluno que deseja ver a média:")
    posicao = verifica_aluno(lista_alunos,nome)
    if posicao != -1:
        soma_notas = 0
        for i in range(len(lista_alunos[posicao].nota)):
            soma_notas += lista_alunos[posicao].nota[i]
        media = soma_notas//len(lista_alunos[posicao].nota)
        print(f"\nMédia de {nome}: {media}")
    else:
        print("\nEsse aluno não está cadastrado!")

def maior_menor_nota(lista_alunos):
    nome = input("\nDigite o nome do aluno que deseja ver a maior e a menor nota:")
    posicao = verifica_aluno(lista_alunos,nome)
    if posicao != -1:
        lista_alunos[posicao].nota = list(lista_alunos[posicao].nota)
        maior = lista_alunos[posicao].nota[0]
        menor = lista_alunos[posicao].nota[0]
        for i in range(len(lista_alunos[posicao].nota)):
            if lista_alunos[posicao].nota[i] > maior:
                maior = lista_alunos[posicao].nota[i]
            if lista_alunos[posicao].nota[i] < menor:
                menor = lista_alunos[posicao].nota[i]
        print(f"\nSegundo notas de {nome}: Maior nota: {maior} | Menor nota: {menor}")
    else:
        print("\nEsse aluno não está cadastrado!")

def gravar_dados_arquivo(nome_arquivo,lista_alunos):
    arq = open(nome_arquivo,'w')
    for y in range(len(lista_alunos)):
        lista_notas = ""
        for i in range(len(lista_alunos[y].nota)):
            if i != 0:
                lista_notas += ", "
            lista_notas += str(lista_alunos[y].nota[i])
        arq.write(lista_alunos[y].nome + ";" + lista_notas + "\n")
    arq.close()

def carregar_arquivo(nome_arquivo):
    lista_de_alunos = []

    if existe_arquivo(nome_arquivo):
        arq = open(nome_arquivo,'r')
        for linha in arq:
            notas = []
            infos = linha.split(";")
            al = Aluno()
            al.nome = infos[0]
            for elemento in infos[1].split(", "):
                notas.append(int(elemento))
            al.nota = notas
            lista_de_alunos.append(al)
        arq.close()
    return lista_de_alunos

def existe_arquivo(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False

def main():
    arquivo_alunos = "./dados_alunos.txt"
    alunos = carregar_arquivo(arquivo_alunos)
    op = 1
    while op != 0:
        op = menu_opcoes()
        if op == 1:
            cadastro_notas(alunos)
        elif op == 2:
            imprimir_alunos(alunos)
        elif op == 3:
            nome_mais_6notas(alunos)
        elif op == 4:
            ver_media(alunos)
        elif op == 5:
            maior_menor_nota(alunos)
        elif op == 0:
            print("Saindo do programa...")
            gravar_dados_arquivo(arquivo_alunos,alunos)  # gravando dados no arquivo
        else:
            print("Opção inválida!")
main()