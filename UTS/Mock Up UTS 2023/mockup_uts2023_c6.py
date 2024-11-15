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
    print(f"\"{names[0]}, {names[1]} and {x-2} others like this\"")
