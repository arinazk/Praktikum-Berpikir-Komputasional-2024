n =100
i = 1
hampiran = 0

for j in range (n):
    if j % 2 == 0: 
        hampiran += 1/(i)
    else:
        hampiran -= (1/(i))
    
    i+=2

print(hampiran*4)