# Soal Praktikum 3 Tahun 2021

N = int(input("Masukkan N: "))
batas = N//2
array = []

for i in range (2, batas + 1):
    if N%i == 0:
        N/=i
        array.append(i)
    else:
        i+=1

print("Faktor primanya adalah ", end="")
for j in range (len(array)):
    print(f"{array[j]} ", end="")