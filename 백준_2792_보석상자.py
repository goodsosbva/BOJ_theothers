n, m = map(int, input().split())

jewels = []
for i in range(m):
    jewels.append(int(input()))

l = 1
r = max(jewels)

cnt = 1
while l < r:
    m = (l + r) // 2
    isAns = True
    total_people_needed = 0


    for jew in jewels:
        people_needed = (jew + m - 1) // m
        total_people_needed += people_needed
            


        if total_people_needed > n:
            isAns = False
            break

    if isAns:
        r = m
    else:
        l = m + 1


print(l)
   
   


            


    
