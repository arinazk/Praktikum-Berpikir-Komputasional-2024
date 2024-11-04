N = int(input())

if N <= 50 and N >= 45:
    print("Atlit bertanding di kelas A.")
elif N <= 55 and N > 50:
    print("Atlit bertanding di kelas B.")
elif N <= 60 and N > 55:
    print("Atlit bertanding di kelas C.")
elif N <= 65 and N > 60:
    print("Atlit bertanding di kelas C.")
elif N <= 70 and N > 65:
    print("Atlit bertanding di kelas D.")
elif N > 70:
    print("Atlit bertanding di kelas E.")
else:
    print("Tidak memenuhi kualifikasi.")