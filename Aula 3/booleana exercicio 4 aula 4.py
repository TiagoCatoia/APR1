num = int(input("Digite uma número para verificar se ele é primo:"))
if num > 1:
    primo = True 
    i = 2
    while i < num and primo == True:
        if num % i == 0:
            primo = False
        i += 1
    
    if primo == True:
        print(num,"é primo")
    else:
        print(num,"não é primo")

if num == 1 or num == 0:
    print(num,"não é primo")
