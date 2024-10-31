A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))
sum = 0

for i in range (A, B+1):
    if i%x == 0 and i%y == 0:
        sum+=i

print(sum)