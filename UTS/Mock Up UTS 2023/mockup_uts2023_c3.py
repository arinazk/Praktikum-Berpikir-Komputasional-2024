A = float(input("Masukkan nilai A: "))
B = float(input("Masukkan nilai B: "))
K = int(input("Masukkan nilai K: "))
x = float(input("Masukkan nilai x: "))
hasil = x

for i in range (K):
    hasil = A*hasil + B

    if hasil < 0:
        hasil = hasil (-1)

print(f"Nilai dari fungsi Pak Ganesh adalah {hasil}")

# p.s. : contoh program salah, hasil = 30 jika K = 3