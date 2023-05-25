N = int(input("Digite o valor de N:"))
M = -1
i = 0
soma = 0
print("Termos da série: ")
while i < N:
    soma = soma + (i/M)
    M = M + 2
    i = i + 1
    print(i,"/",M)

print(f"Soma total da série: {soma:.2f}")
