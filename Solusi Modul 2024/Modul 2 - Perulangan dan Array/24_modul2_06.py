# Soal Praktikum 1 Tahun 2021

potongan = int(input("Masukkan banyak potongan lego: "))
batasan = potongan // 3 + 1
akar = 0
nilai = 0
sementara = 0
sisa = potongan
banyak = 0
i = 1

while sisa >= 0: 
    while i**3 <= sisa:
        if i**3 > sisa:
            break

        if i**3 <= sisa:
            sementara = i**3
            if sementara >= nilai:
                nilai = sementara
                banyak+=1
    
        i+=1
    print(f"{nilai}")
    sisa = sisa - nilai

print(f"Tuan Leo dapat membuat {banyak} kubus.")