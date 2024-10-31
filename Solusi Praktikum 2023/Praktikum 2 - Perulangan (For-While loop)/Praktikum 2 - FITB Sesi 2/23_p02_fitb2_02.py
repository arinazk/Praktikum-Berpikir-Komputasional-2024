x = int(input("Masukkan nilai x: "))
i = 0

while x >= 1:
    if x%2 == 0:
        x/=2
    elif x%2 == 1:
        x=x*3+1

    i+=1

    if x == 1:
        break

print(f"Terjadi {i} iterasi.")