N = int(input("Masukkan N: "))
bb_semua = [0 for i in range (N)]

for i in range (N):
    arr =[] # Array berat badan petinju ke-i
    arr = input(f"Masukkan berat petinju ke-{i+1}: ")
    x = len(arr)
    tanda = False
    bb = []
    for j in range (x):
        # Mengenali berat badan petinju ke-1
        if arr[j] == '0' or arr[j] == '1' or arr[j] == '2' or arr[j] == '3' or arr[j] == '4' or arr[j] == '5' or arr[j] == '6' or arr[j] == '7' or arr[j] == '8' or arr[j] == '9':
            bb += [int(arr[j])]
        elif arr[j] == 'k': # Mengenali kg atau lb
            tanda = True
    
    y = len(bb)
    bb_sementara = 0
    # Mengenali int berat bedan petinju ke-i
    for k in range (y-1, -1, -1):
        bb_sementara += bb[k]*(10**(y-k-1))
    
    if tanda == True:
        bb_sementara*=2.205 # Jika bb dalam kg, ubah nilai ke lb
    
    bb_semua[i] = bb_sementara # Mengganti nilai bb_semua indeks ke i

for i in range (N):
    if bb_semua[i] >= 200:
        print(f"Petinju ke-{i+1} masuk ke dalam kelas Heavyweight")
    elif 154 <= bb_semua[i] < 200:
        print(f"Petinju ke-{i+1} masuk ke dalam kelas Middleweight")
    else:
        print(f"Petinju ke-{i+1} masuk ke dalam kelas Lightweight")
