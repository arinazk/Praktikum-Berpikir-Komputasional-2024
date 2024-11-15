N = int(input("Masukkan nilai N: "))

# Menghitung nilai faktorial
faktorial = N
for i in range (N-1, 0, -1): 
    faktorial*=i

faktorial_str = str(faktorial)
x = len(faktorial_str)
count = 0

# Mencari nilai 0 berurutan yang menghakhiri N!
j = 1
while faktorial_str[x-j] == '0': # Berhenti jika menemukan faktorial_str[x-j] tidak sama dengan 0
    count+=1
    j+=1

print(f"0 berurutan yang mengakhiri {N}! sebanyak {count} buah")