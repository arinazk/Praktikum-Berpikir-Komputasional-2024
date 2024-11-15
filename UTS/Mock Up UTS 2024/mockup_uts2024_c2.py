bilangan = [0 for i in range (3)]
bilangan_maks = 0
for i in range (3):
    bilangan[i] = float(input(f"Masukkan bilangan ke-{i+1}: "))
    if bilangan_maks == 0 or bilangan_maks <= bilangan[i]:
        bilangan_maks = bilangan[i]

print(f"Bilangan terbesar adalah {bilangan_maks}")