# Palindrom

panjang = int(input("Masukkan panjang string: "))
string = (input("Masukkan string: "))
array = []
bool = True

for char in string:
    array.append(char)

for i in range (panjang):
    if array[i] != array[panjang-1-i]:
        bool = False

if bool == False:
    print(f"{string} bukan palindrom")
else:
    print(f"{string} adalah palindrom")