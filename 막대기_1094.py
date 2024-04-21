x = int(input())

cnt = 1
candi = [64]
while True:
    if sum(candi) > x:
        stick = candi.pop(-1)
    
    elif sum(candi) < x:
        cnt += 1

    elif sum(candi) == x:
        break

    stick = stick / 2
    candi.append(stick)

print(cnt)