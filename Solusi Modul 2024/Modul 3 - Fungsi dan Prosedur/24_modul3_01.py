def fungsi(x):
    y = x**2 - 2*x + 5
    return y

A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

for i in range (A, B+1):
    n = fungsi(i)
    print(f"f({i}) = {n}")