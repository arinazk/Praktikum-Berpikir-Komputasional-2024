L = float(input("Masukkan L: "))
x = int(input("Masukkan sudut: "))
panjang = 0

# Menghitung phi 
n =100
a = 1
hampiran_phi = 0
for i in range (n):
    if i % 2 == 0: 
        hampiran_phi += 1/(a)
    else:
        hampiran_phi -= (1/(a))
    
    a+=2
hampiran_phi*=4

# Menghitung sin(x)
b = 1
hampiran_sin = 0
x = x/180*hampiran_phi
for i in range (1, n+1, 1):
    faktorial = b
    for j in range (b-1, 0, -1):
        faktorial*=j
    
    if i % 2 ==0:
        hampiran_sin += (x**b) / faktorial
    else:
        hampiran_sin -= (x**b) / faktorial
    
    b+=2

print(hampiran_phi)
print(hampiran_sin)
panjang_lintasan = 2*hampiran_phi*L*hampiran_sin
print(panjang_lintasan)