ayah = input("Masukkan alel dari ayah: ")
ibu = input("Masukkan alel dari ibu: ")

if ayah[1] == 'O' and ibu[1] == 'O':
    print("O")
elif (ayah[1] == 'B' and ibu[1] == 'O') or (ayah[1] == 'O' and ibu[1] == 'B') or (ayah[1] == 'B' and ibu[1] == 'B'):
    print("B")
elif (ayah[1] == 'A' and ibu[1] == 'O') or (ayah[1] == 'O' and ibu[1] == 'A') or (ayah[1] == 'A' and ibu[1] == 'A'):
    print("A")
elif (ayah[1] == 'A' and ibu[1] == 'B') or (ayah[1] == 'B' and ibu[1] == 'A'):
    print("AB")