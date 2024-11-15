arr = [0 for i in range (50)]
terbesar = 0

print("Masukkan data berat badan siswa = ")
for i in range (50):
    arr[i]=int(input())
    if arr[i] >= terbesar:
        terbesar = arr[i]
print(f"Berat badan terbesar = {terbesar}")

x = int(input("Masukkan berat badan = "))
count = 0
lebih_dari_x = []
for i in range(50):
    if arr[i] > x:
        count+=1
        lebih_dari_x += [arr[i]]

print(f"Banyaknya siswa dengan berat > {x} = {count}")
if count>0:
    print(f"Daftar berat badan > {x} = ")
    for i in range (count):
        print(lebih_dari_x[i])