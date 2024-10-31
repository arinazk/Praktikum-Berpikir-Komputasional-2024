N = int(input("Masukkan nilai N: "))
n = [0 for i in range (N)]
potongan = 0

for i in range (N):
    n[i] = int(input(f"Masukkan bilangan ke-{i+1}: "))

for i in range (N):
    for j in range (0, i+1):
        sum = 0
        lst = []

        for k in range (j, i+1): 
            sum += n[k]
            lst.append(n[k])

        if sum>1:
            bool = True
            batas = sum//2 + 1
            for l in range (2, batas):
                if sum%l == 0:
                    bool = False
                    break

            if bool == True: 
                potongan+=1
                print(lst)

print(potongan)