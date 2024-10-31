N = int(input("Masukkan nilai N: "))
jam = [0 for i in range (N)]
sementara = 0
sum = 0

for i in range (N):
    jam[i] = int(input(f"Masukkan harga jam ke-{i+1}: "))

for i in range (N-1, 1, -1):
    sementara = jam[i] + jam[i-1] + jam[i-2]
    if sum == 0:
        sum = sementara
    elif sum >= sementara:
        sum = sementara

print(f"Total harga yang harus dibayar adalah {sum}")