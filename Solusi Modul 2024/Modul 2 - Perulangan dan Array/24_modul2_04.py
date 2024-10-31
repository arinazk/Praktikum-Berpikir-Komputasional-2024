# Anagram

A = int(input("Masukkan banyaknya elemen A: "))
a = [0 for i in range (A)]

for i in range (A):
    a[i] = int(input(f"Masukka elemen A ke-{i+1}: "))

B = int(input("Masukkan banyaknya elemen B: "))
b = [0 for i in range (B)]

for j in range (B):
    a[j] = int(input(f"Masukka elemen B ke-{i+1}: "))

if A!=B:
    print("B bukanlah anagram dari A")
    exit()

tandaiA = tandaiB = 0
for i in range (A):
    for j in range (B):
        if a[i] == b[j]:
            tandaiA+=1

for i in range (B):
    for j in range (A):
        if b[i] == a[j]:
            tandaiB+=1

if tandaiA == tandaiB:
    print("B adalah anagram dari A")
else:
    print("B bukanlah anagram dari A")
    

