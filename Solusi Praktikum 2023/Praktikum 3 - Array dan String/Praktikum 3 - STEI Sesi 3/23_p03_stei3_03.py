panjang_asli = int(input("Masukkan panjang kata asli: "))
kata_asli = input("Masukkan kata asli: ")
panjang_tulis = int(input("Masukkan panjang kata yang ditulis: "))
kata_tulis = input("Masukkan kata yang ditulis: ")

array_kata = kata_asli.split()

lst = []
for i in range (panjang_asli):
    for j in range (0, i+1):
        lst.append(kata_asli[j])

panjang = len(lst)
if panjang_tulis != panjang:
    print("Salah")
elif panjang_tulis == panjang:
    jumlah_benar = 0
    for i in range (panjang):
        if kata_tulis[i] != lst[i]:
            break
        elif kata_tulis[i] == lst[i]:
            jumlah_benar+=1
    
    if jumlah_benar == panjang:
        print("Benar")
else:
    print("Salah")
