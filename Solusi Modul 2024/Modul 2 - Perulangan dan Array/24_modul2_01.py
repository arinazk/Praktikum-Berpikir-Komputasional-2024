# Kelipatan 10 Terkecil

N = int(input("Masukkan N: "))
x = 10

while x < N:
    x*=10
    if x > N:
        break

print(x)
