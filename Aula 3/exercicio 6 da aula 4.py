nota = int(input("Digite a nota do aluno (negativo para sair): "))
contador = 0    #contador = quantidade total de notas
soma = 0
contador_maiorigual_seis = 0
contador_maiorigual_quatro_menor_seis = 0
contador_menor_quatro = 0
while nota >= 0:
    if nota >= 6:
        contador_maiorigual_seis += 1
    elif 4 <= nota < 6:
        contador_maiorigual_quatro_menor_seis += 1
    else:
        contador_menor_quatro += 1
    contador = contador + 1
    soma = soma + nota
    nota = int(input("Digite a nota do aluno (negativo para sair): "))

media = soma/contador
if nota < 0:
    print("Quantidade de notas maiores ou iguais a seis: ",contador_maiorigual_seis)
    print("Quantidade de notas iguais a quatro ou cinco: ",contador_maiorigual_quatro_menor_seis)
    print("Quantidade de notas menores que quatro: ",contador_menor_quatro)
    print(f"Media das notas: {media:.2f}")
