plat = input("Masukkan nomor plat mobil: ")
jumlah_digit = int(input("Masukkan jumlah digit: "))
banyak_digit = int(input("Masukkan banyak digit: "))
sum = 0
number = 0

if plat[0] != 'D':
    print("Bukan mobil Tuan Kil!")
    exit()

for char in plat[1:]:  # Mulai dari indeks 1 (mengabaikan 'D')
    if '0' <= char <= '9':  # Memeriksa apakah karakter adalah digit
        angka = int(char)
        sum += angka
        number += 1

if sum == jumlah_digit and number == banyak_digit:
    print("Mobil Tuan Kill ditemukan!")
else:
    print("Bukan mobil Tuan Kil!")
