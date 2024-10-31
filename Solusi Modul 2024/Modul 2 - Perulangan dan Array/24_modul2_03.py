# Reverse

N = int(input("Masukkan N: "))
n = [0 for i in range (N)]

for i in range (N):
    n[i] = int(input())

print("Hasil dibalik:")
for i in range (N-1, -1, -1):
    print(f"{n[i]} ", end="")