#COM BREACK
cont = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","desseseis","dessesete","dezoito","dezenove","vinte")
while True:
    num = int(input("Digite um número de 0 a 20 para ver por extenso:"))
    if num >= 0 and num <= 20:
        break
    print("O número digitado não está entre 0 e 20, tente novamente!")
print(f"Você digitou o número {cont[num]}")

#SEM BRACK
cont = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","desseseis","dessesete","dezoito","dezenove","vinte")
entre_0_e_20 = False
while entre_0_e_20 == False:
    num = int(input("Digite um número de 0 a 20 para ver por extenso:"))
    if num >= 0 and num <= 20:
        entre_0_e_20 = True
    if entre_0_e_20 == False:
        print("O número digitado não está entre 0 e 20, tente novamente!")
print(f"Você digitou o número {cont[num]}")