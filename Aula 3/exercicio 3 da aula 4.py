#com for
for y in range(1,11):
    print("Tabuada do", y, ":")
    for t in range(1,11):
        print(y, "x", t, "=", y*t)
    print("\n")


#com while
y = 1
while y <= 10:
    print("Tabuada do", y, ":")
    t = 1
    while t <= 10:
        print(y, "x", t, "=", y*t)
        t = t + 1
    print("\n")
    y = y + 1
    
