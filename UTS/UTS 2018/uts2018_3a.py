N = int(input())
sum = 0
count = 0

if N != -999:
    while N != -999:
        if N >= 100 and N <=200:
            sum+=N
            count+=1

        N = int(input())

if count > 0:
    avg = sum/count
    print(avg)
else: 
    print("Tidak ada data")