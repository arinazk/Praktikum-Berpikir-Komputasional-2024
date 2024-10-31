N = int(input("Masukkan nilai N: "))
i = 1

availA = 5
availB = 3
pakaiA = 0
pakaiB = 0

while True:
    peserta = int(input(f"Masukkan peserta kegiatan ke-{i}: "))

    if availA != 0 and availB != 0:
        if peserta>=N:
            pakaiB+=1
            availB-=1
        else:
            pakaiA+=1
            availA-=1
    elif availA == 0 and availB !=0:
        pakaiB+=1
        availB-=1

    if availB == 0:
        break
    
    i+=1

print(f"Terdapat {pakaiA} kegiatan di gedung A dan {pakaiB} kegiatan di gedung B")