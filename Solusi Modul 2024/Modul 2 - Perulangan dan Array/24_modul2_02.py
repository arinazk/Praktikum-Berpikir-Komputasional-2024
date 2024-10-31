# Segitiga Angka

N = int(input("Masukkan N: "))

for i in range (1, N+1):
    for j in range (1, i+1):
        print(f"{j} ", end="")
    print()
