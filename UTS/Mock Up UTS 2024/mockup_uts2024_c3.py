N = int(input("Masukkan N: "))
faktorial = N

for i in range (N-1, 0, -1):
    faktorial*=i

print(faktorial)