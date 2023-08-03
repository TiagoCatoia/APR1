str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")
str1 = str1.lower()
str2 = str2.lower()

i = 0
while i < len(str1):
    if str1[i] == " ":
        str1 = str1[:i] + str1[i+1:]
    i += 1
i = 0
while i < len(str2):
    if str2[i] == " ":
        str2 = str2[:i] + str2[i+1:]
    i += 1

if len(str1) != len(str2):
    print("Não são anagrama!")
else:
    i = -1
    t = 0
    anagrama = True
    while i > -len(str1) and anagrama:
        if str1[i] != str2[t]:
            anagrama = False
        t += 1
        i -= 1
if anagrama:
    print("São anagrama!")
else:
    print("Não são anagrama")