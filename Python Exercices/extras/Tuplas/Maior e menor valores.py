from random import randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),) #sortei 5 num aletórios e coloque em uma tupla
print(f"Eu sortieei os números {num}")
print(f"O maior número é o {max(num)}")
print(f"O menor número é o {min(num)}")