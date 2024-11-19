def diskriminan (a, b, c):
    return b**2-4*a*c

def jenis_akar(d):
    d = diskriminan(a, b, c)
    print(f"Nilai diskriminan: {d:.2f}")
    if d > 0:
        print("Persamaan kuadrat memiliki akar kembar")
    elif d == 0:
        print("Persamaan kuadrat memiliki akar real kembar")
    else:
        print("Persamaan kuadrat tidak memiliki akar real")
    return

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

d = diskriminan(a,b,c)
jenis_akar(d)