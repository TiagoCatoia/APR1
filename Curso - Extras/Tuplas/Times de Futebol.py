times = ('Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Grêmio', 'Internacional',
    'Cruzeiro', 'Atlético Mineiro', 'Corinthians', 'Fluminense', 'Botafogo',
    'Vasco da Gama', 'Bahia', 'Sport Recife', 'Fortaleza', 'Ceará', 'Atlético Paranaense',
    'Goiás', 'Chapecoense', 'Avaí')
print("Lista dos 20 primeiros colocardos:")
for time in times:
    print(f"{time},",end=" ")
print("\n")
print("Cinco primeiros colocados:",times[:6])
print("\n")
print("Os 4 últimos colocados:", times[16:])
print("\n")
print("Times em ordem alfabética:", sorted(times))
print("\n")
print(f"Posição do Chapecoense: {times.index('Chapecoense')+1}º posição")