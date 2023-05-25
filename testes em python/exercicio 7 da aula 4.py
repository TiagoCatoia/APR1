#N + 1 = N + N - 1

anterior = 0
proxima = 1
soma = 1
for n in range(8):
    print(anterior)
    soma = anterior + proxima
    anterior = proxima
    proxima = soma
  
