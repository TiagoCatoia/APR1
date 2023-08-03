from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
jogo["jogador 1"] = randint(1,6) #dado 1
jogo["jogador 2"] = randint(1,6) #dado 2
jogo["jogador 3"] = randint(1,6) #dado 3
jogo["jogador 4"] = randint(1,6) #dado 4
for k, v in jogo.items():
    print(f"O {k} tirou o número {v} no dado")
    sleep(1)
ranking = list() #como ranking é uma lista podemos utilizar o enumerate que acessa o índice e o valor de cada elemento da lista/tupla
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #itemgetter(1) o parametro (1) especifica a ordem pelo valor, se fosse 0 seria pela chave
print("-=" * 30)
for i, v in enumerate(ranking):
    print(f"  {i+1}º Lugar {v[0]} tirou {v[1]} ")
    sleep(1)