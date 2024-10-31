n = int(input("Masukkan banyak segitiga: "))
batas = n*4+1

for i in range (3):
    if i == 0:
        for j in range (1, batas+1):
            print("*", end="")
        
        print()
    if i == 1:
        for j in range (1, batas):
            if j%4==1:
                print(" ", end="")
            else:
                print("*", end="")
        
        print()
    if i == 2:
        for j in range (1, batas-1):
            if j <= 3:
                if j%3 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                j-=3
                if j%4 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
        
        print()
