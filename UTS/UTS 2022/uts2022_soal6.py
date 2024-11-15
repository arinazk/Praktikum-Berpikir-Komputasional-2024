n = int(input("Masukkan n: "))
tanda = False

for i in range (2, n):
    if (n%i) == 0:
        tanda = True

if tanda:
    print(f"{n} bukan bilangan prima")
else:
    print(f"{n} adalah bilangan prima")