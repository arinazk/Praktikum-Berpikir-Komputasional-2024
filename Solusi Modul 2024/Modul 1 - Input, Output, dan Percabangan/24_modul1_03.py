N = int(input("Masukkan sebuah bilangan: "))
ribuan = N // 1000
ratusan = (N - (ribuan*1000)) // 100
puluhan = (N - (ribuan*1000) - (ratusan*100)) // 10
satuan = N % 10
sum = ribuan + ratusan + puluhan + satuan

if sum % ribuan == 0 and sum % ratusan == 0 and sum % puluhan == 0 and sum % satuan == 0:
    print("Bilangan tersebut adalah bilangan Bravo")
else:
    print("Bilangan tersebut adalah bilangan biasa")