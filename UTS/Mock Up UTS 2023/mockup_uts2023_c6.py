names = ["Alex", "Jacob", "Mark", "Max"] # Inisiasi array
x = len(names)

if x == 0:
    print("\"no one likes this\"")
elif x == 1:
    print(f"\"{names[0]} likes this\"")
elif x == 2:
    print(f"\"{names[0]} and {names[1]} like this\"")
elif x == 3:
    print(f"\"{names[0]}, {names[1]}, and {names[2]} like this\"")
else:
    for i in range (x):
        if i == x-1:
            print(f"and {names[i]} like this\"")
        elif i == x-2 :
            print(f"{names[i]} ", end="")
        elif i == 0:
            print(f"\"{names[i]}, ", end="")
        else: 
            print(f"{names[i]}, ", end="")