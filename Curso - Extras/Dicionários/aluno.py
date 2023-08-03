nome = input("Digite o nome do aluno:")
media = float(input(f"Digite a média de {nome}:"))
aluno = {}
aluno["Nome"] = nome
aluno["Media"] = media
if aluno["Media"] >= 6:
    aluno["Situacao"] = "Aprovado"
else:
    aluno["Situacao"] = "Reprovado"

print("-=" * 30)
print(f"  - Nome do aluno: {aluno['Nome']}")
print(f"  - Média: {aluno['Media']}")
print(f"  - Situação: {aluno['Situacao']}")