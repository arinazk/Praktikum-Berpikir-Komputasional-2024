panjang = float(input("Masukkan panjang gelombang: "))

if 380 <= panjang <=450:
    print("Ungu")
elif 451 <= panjang <= 495:
    print("Biru")
elif 496 <= panjang <= 570:
    print("Hijau")
elif 571<=panjang <= 590:
    print("Kuning")
elif 591 <= panjang <= 620:
    print("Jingga")
elif 621 <= panjang <=750:
    print("Merah")
else:
    print("Warna tidak terdefinisi.")