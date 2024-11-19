def perkalian(n):
    n_str = str(n)
    x = len(n_str)
    sum = 1
    for i in range (x):
        sum *= int(n_str[i])
    return sum

n = int(input("Masukkan sebuah bilangan: "))
i = 1

while n >= 10:
    n = perkalian(n)
    print(f"Setelah proses ke-{i}: {n}")
