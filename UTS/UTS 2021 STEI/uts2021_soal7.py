a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
x = int(input("Masukkan x: "))
n = int(input("Masukkan n: "))

sum = 0

for i in range (1, n+1, 1):
    f = a*(x**i)+b
    sum+=f

print(f)