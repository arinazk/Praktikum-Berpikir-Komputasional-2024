def ubah_huruf(j, x, tanda):
    alp = "abcdefghijklmnopqrstuvwxyz"
    if tanda == 1:
        return alp[(j - x) % 26]
    else:
        return alp[(j + x) % 26]

def ubah_pesan(pesan, n, x, tanda):
    alp = "abcdefghijklmnopqrstuvwxyz"
    pesan_baru = []
    for i in range (n):
        if pesan[i] == ' ':
            pesan_baru += ' '
        else:
            for j in range (26):
                if pesan[i] == alp[j]:
                    huruf_baru = ubah_huruf(j, x, tanda)
                    pesan_baru += [huruf_baru]
    return pesan_baru
    
tipe = input("Masukkan tipe pesan: ")
pesan = input("Masukkan pesan: ")
x = int(input("Masukkan nilai x: "))
n = len(pesan)

if tipe == "enkripsi":
    tanda = 1
else:
    tanda = 2

hasil = ubah_pesan(pesan, n, x, tanda)
for i in range (n):
    print(f"{hasil[i]}", end="")


