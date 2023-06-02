idade = int(input("Digite a idade do eleitor: "))
if idade == 16:
    print("Voto facultativo")
elif idade == 17:
    print("Voto facultativo")
elif idade <= 15:
    print("Eleitor não possui idade para votar")
elif idade >=66:
    print("Eleitor dispensado de votar")
else:
    print("Voto obrigatório")

