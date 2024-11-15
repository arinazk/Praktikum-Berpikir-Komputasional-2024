sentence = input()
x = len(sentence)
kecil = "abcdefghijklmnopqrstuvwxyz"
kapital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
detect = [False for i in range (26)]

if x < 26:
    print("No")
else: 
    for i in range (x):
        for j in range (26):
            if sentence[i] == kecil[j] or sentence[i] == kapital[j]:
                detect[j] = True

count = 0
for i in range (26):
    if detect[i] == True:
        count+=1

if count == 26:
    print("Armstrong")
else:
    print("Not an armstrong")

