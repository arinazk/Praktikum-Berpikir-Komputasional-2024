# Blok ini tidak perlu dibuat
N = int(input("Masukkan N:"))
arr = [0 for i in range (N)]
print("Masukkan array: ")
for i in range (N):
    arr[i] = int(input())

# Blok yang diminta dibuat oleh soal
banyak = 0
for i in range (N):
    if arr[i] > 0 and arr[i]%2 == 0:
        banyak+=1

print(banyak)