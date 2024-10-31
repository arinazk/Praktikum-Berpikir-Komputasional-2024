N= int(input("Masukkan banyak nilai: "))
terkecil1 = 0
status1 = True
terkecil2 = 0
status2 = True

for i in range (1, N+1):
    nilai = float(input(f"Masukkan nilai ke-{i}: "))

    if status1 == False and status2 == False:
        i
        if nilai < terkecil1:
            terkecil1 = nilai
        elif nilai < terkecil2:
            terkecil2 = nilai
    elif status1 == True:
        terkecil1=nilai
        status1 = False
    elif status2 == True:
        terkecil2=nilai
        status2 = False

ratarata = (terkecil1 + terkecil2)/2
print("Rata-rata 2 nilai terkecil adalah ", ratarata)