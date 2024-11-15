N = int(input("Masukkan N: "))
fibonacci = [0 for i in range (N)]

print("Deret fibonacci : ", end="")
fibonacci[0] = 0
print(f"{fibonacci[0]} ", end="")
fibonacci[1] = 1
print(f"{fibonacci[1]} ", end="")
for i in range (2, N):
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]
    print(f"{fibonacci[i]} ", end="")
    