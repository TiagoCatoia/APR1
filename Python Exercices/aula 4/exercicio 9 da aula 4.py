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


# OU

n = int(input("Informe o número de termos da série:"))
num = 1
den = 1
s = 0
print("S =", end=" ")
while num<=n:
    if num == n:
        print("f {num}/{den}",end=" ")
    else:
        print(f"f{num}/{den} +",end=" ")
    print("f {num}/{den} +",end=" ")
    s = s + (num/den)
    num += 1
    den += 2
print("f\nResultado final: {s:.2f}")