N = int(input("Masukkan panjang array: "))
arr = [0 for i in range (N)]
x = 5 #Bilangan yang dicari
tanda = False

for i in range (N):
    arr[i] = float(input(f"Masukkan bilangan ke-{i+1}: "))
    if arr[i] == x:
        print(i)
        tanda = True

if tanda == False:
    print("Bilangan tidak ditemukan")
