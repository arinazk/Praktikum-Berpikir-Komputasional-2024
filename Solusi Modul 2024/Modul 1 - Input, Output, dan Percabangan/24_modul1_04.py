x_awal = int(input("Masukkan koordinat katak: "))
a = int(input("Masukkan panjang lompatan katak ke kanan: "))
b = int(input("Masukkan panjang lompatan katak ke kiri: "))

if x_awal < 0 and x_awal % 3 == 0:
    k = b*2
elif (x_awal >= 0 and x_awal % 2 == 0) or (x_awal < 0):
    k = a * b
else:
    k = a*2

if k % 2 == 0:
    x_akhir = x_awal + (k/2) * a - k/2 * b
else:
    x_akhir = x_awal + (k//2 + 1) * a - k//2 * b

print("Koordinat katak sekarang adalah ", int(x_akhir))