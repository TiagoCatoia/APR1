''' Segunda prova prática de Algoritmos e Programação 1 (APR1) - 01-06-2023
    Coloque aqui seu nome e o prontuário.
    Tiago Catoia de Souza SC3038289
    ATENÇÃO: PROVA SEM CONSULTA
'''

class Aluno():
        nome = ""
        serie = -1
        mat = -1
        port = -1
        cien = -1
        hist = -1
        geo = -1
        media = -1

def menu():
    print("Segunda prova prática de APR1 - 01-06-2023")
    print("Escolha uma das opções a seguir:")
    print("1. Imprimir palavra em formato de escada")
    print("2. Verificar se uma frase é um palíndromo")
    print("3. Imprimir o elemento MINMAX de uma matriz")
    print("4. Submenu Notas de Alunos")
    print("0. Encerrar o programa")
    op = int(input(""))
    return op

def submenu_notas(notas_alunos):
    print("Escolha uma das opções a seguir ou digite outro valor para voltar ao menu principal:")
    print("1. Cadastrar uma nota de prova de um aluno")
    print("2. Imprimir dados de todos os alunos")
    print("0. Sair do submenu")
    #print("3. Imprimir média geral em ordem decrescente de média")
    op = input("Entre com a opção desejada:")
    while op != "0":
        if op == "1":
            print("Cadastrando uma nota de prova de um aluno...")        
            cadastro(notas_alunos)
        elif op == "2":
            print("Imprimindo os dados de todos os alunos...")
            consultar_tds_alunos(notas_alunos)
        #elif op == "3":
        #   print("Imprimir média geral em ordem decrescente de média...")        
        else:
            print("Saindo do submenu...") 
        print("Escolha uma das opções a seguir ou digite outro valor para voltar ao menu principal:")
        print("1. Cadastrar uma nota de prova de um aluno")
        print("2. Imprimir dados de todos os alunos")  
        op = input("Digite uma nova opção (1 ou 2) ou digite 0 para sair do submenu:")

def cadastro(notas_alunos):
    al = Aluno()
    al.nome = input("Digite o nome completo do aluno:")
    if verificar_aluno(notas_alunos,al.nome) == -1:
        print("Aluno não cadastrado, cadastrando aluno...")
        al.serie = int(input("Digite a série atual do aluno:"))
        al.mat = int(input("Digite a nota de matemática do aluno:"))
        al.port = int(input("Digite a nota de português do aluno:"))
        al.cien = int(input("Digite a nota de ciências do aluno:"))
        al.hist = int(input("Digite a nota de história do aluno:"))
        al.geo = int(input("Digite a nota de geografia do aluno:"))
        al.media = (al.mat + al.port + al.cien + al.hist + al.geo)//5
        notas_alunos.append(al)
    else:
        posicao = verificar_aluno(notas_alunos,al.nome)
        print("Aluno já cadastrado, iniciando atualização do cadastro...")
        notas_alunos[posicao].serie = int(input("Digite a série atual do aluno:"))
        notas_alunos[posicao].mat = int(input("Digite a nota de matemática do aluno:"))
        notas_alunos[posicao].port = int(input("Digite a nota de português do aluno:"))
        notas_alunos[posicao].cien = int(input("Digite a nota de ciências do aluno:"))
        notas_alunos[posicao].hist = int(input("Digite a nota de história do aluno:"))
        notas_alunos[posicao].geo = int(input("Digite a nota de geografia do aluno:"))
        notas_alunos[posicao].media = (notas_alunos[posicao].mat + notas_alunos[posicao].port + notas_alunos[posicao].cien + notas_alunos[posicao].hist + notas_alunos[posicao].geo)//5

def verificar_aluno(notas_alunos,nome):
    i = 0
    while i < len(notas_alunos):
        if notas_alunos[i].nome == nome:
            return i
        i += 1
    return -1

def consultar_tds_alunos(notas_alunos):
    if len(notas_alunos) != 0:
        i = 0
        while i < len(notas_alunos):
            print(f"Nome: {notas_alunos[i].nome}  |  Série: {notas_alunos[i].serie}  | Média:{notas_alunos[i].media}  | Notas: matemática:{notas_alunos[i].mat} português:{notas_alunos[i].port} ciências:{notas_alunos[i].cien} história:{notas_alunos[i].hist} geografia:{notas_alunos[i].geo}")
            i += 1
    else:
        print("Não existe nenhum aluno cadastrado!")

def escada(pal):
    i = 0
    while i <= len(pal):
        print(pal[:i])
        i += 1
    i = -1
    while i >= -len(pal):
        print(pal[:i])
        i -= 1

def palindromo(frase):
    i = 0
    t = -1
    palindromo = True
    while i < len(frase) and palindromo == True:
        if frase[i] == " ":
            i += 1
            t -= 1
        if frase[i] != frase[t]:
            palindromo = False
        t -= 1
        i += 1
    if palindromo:
        return 1
    else:
        return -1

def matriz(matriz,lin,col):
    i = 0
    while i < lin:
        print(f"Digite os elementos da linha {i}:")
        linha = []
        j = 0
        while j < col:
            elemento = int(input())
            linha.append(elemento)
            j += 1
        matriz.append(linha)
        i += 1

def minmax(matriz):
    i = 0
    j = 0
    maior = matriz[i][j]
    menor = matriz[i][j]
    while i < len(matriz): # descobre a linha com o menor valor
        j = 0
        while j < len(matriz[i]):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
            j += 1
        i += 1

    i = 0
    while i < len(matriz): # descobre o maior elemento da linha com o menor elemento
        j = 0
        while j < len(matriz[i]):
            if menor == matriz[i][j]:
                j = 0
                while j < len(matriz[i]):
                    if matriz[i][j] > maior:
                        maior = matriz[i][j]
                    j += 1
            j += 1
        i += 1
    i = 0 # print no maior elemento e na sua posição
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            if matriz[i][j] == maior:
                print(f"Posição:{i+1}x{j} e maior elemento:{maior}")
            j += 1
        i += 1

def main():
    Notas_alunos = []
    opcao = menu()
    while opcao != 0:
        if opcao == 1:
            print("Imprimindo uma palavra em formato de escada...")  
            palavra = input("Digite uma palavra:")
            escada(palavra)
        elif opcao == 2:
            print("Verificar se uma frase é um palíndromo...")  
            frase = input("Digite uma frase:")
            if palindromo(frase) == 1:
                print("A frase é um palíndromo")
            else:
                print("A frase não é um palíndromo")      
        elif opcao == 3:
            print("Imprimir o elemento MINMAX de uma matriz...")    
            Matriz = []
            linha = 3
            coluna = 4
            matriz(Matriz,linha,coluna)
            minmax(Matriz)    
        elif opcao == 4:
            print("Gerenciando as Notas dos Alunos...")
            submenu_notas(Notas_alunos)
        elif opcao == 0:
            print("Encerrando o programa...")
        else:
            print("Opção inválida!")
        opcao = int(input("Digite uma nova opção:"))
main()
