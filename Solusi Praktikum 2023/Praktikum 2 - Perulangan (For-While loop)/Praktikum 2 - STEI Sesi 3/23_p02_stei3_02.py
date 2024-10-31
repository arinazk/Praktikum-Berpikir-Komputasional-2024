x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))
a = 1
b = 0
batas = y
sum = 0
i = 0

while i != x:
    if b%2 == 1:
        if a > 1:
            print(f"{a} ", end="")
            a-=1
            i+=1
        elif a==1:
            b+=1
    else: 
        if a%batas == 0:
            b+=1
            batas+=y
        elif a%batas != 0 and b%2==0:
            print(f"{a} ", end="")
            a+=1
            i+=1
