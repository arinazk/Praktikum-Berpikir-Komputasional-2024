N = int(input("N = "))
D1 = [0 for i in range (N)] # atau D1 = [0]*N
D2 = [0 for i in range (N)]

print("D1 = ")
for i in range (N):
    D1[i]= int(input())

print("D2 = ")
for i in range (N):
    D2[i]= int(input())

TP = TN = FP = FN = 0
for i in range (N):
    if D1[i] == D2[i] == 1:
        TP+=1
    elif D1[i] == D2[i] == -1:
        TN+=1
    elif D1[i] == -1 and D2[i] == 1:
        FP+=1
    elif D1[i] == 1 and D2[i] == -1:
        FN+=1

Akurasi = (TP+TN) / (TP+TN+FP+FN)
print(f"TP = {TP}")
print(f"TN = {TN}")
print(f"FP = {FP}")
print(f"FN = {FN}")
print(f"Akurasi = {Akurasi}")