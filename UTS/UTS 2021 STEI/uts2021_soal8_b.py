x = int(input("Masukkan x: "))
euler = 0

print("Perkiraan populasi penduduk kota A")
for i in range (1, x+1, 1):
    sum = i
    for i in range (i-1, 1, -1):
        sum*=i
    
    euler+=1/sum
    print(f"Tahun ke-{i}: {euler} juta")
