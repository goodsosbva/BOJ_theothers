def chkEightDirection(x, y, val, target_length=5):
    if val == 0:
        return [False, -1, -1]

    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    for dx, dy in directions:
        count = 0
        for i in range(target_length):
            nx, ny = x + dx * i, y + dy * i

            if 0 <= nx < len(concavePlate) and 0 <= ny < len(concavePlate[0]) and concavePlate[nx][ny] == val:
                count += 1
            else:
                break

        if count == target_length:
            prev_nx, prev_ny = x - dx, y - dy
            next_nx, next_ny = x + dx * target_length, y + dy * target_length

            if (0 <= prev_nx < len(concavePlate) and 0 <= prev_ny < len(concavePlate[0]) and concavePlate[prev_nx][prev_ny] == val) or \
               (0 <= next_nx < len(concavePlate) and 0 <= next_ny < len(concavePlate[0]) and concavePlate[next_nx][next_ny] == val):
                continue

            return [True, x, y]  

    return [False, -1, -1]


concavePlate = []
for i in range(19):
    con = list(map(int, input().split()))
    concavePlate.append(con)

answer = False
ax = -1
ay = -1

for i in range(19):
    for j in range(19):
        isAnswer = chkEightDirection(i, j, concavePlate[i][j])

        if isAnswer[0]:
            answer = True
            ax = isAnswer[1]
            ay = isAnswer[2]
            break  
    if answer:
        break

if answer:
    print(concavePlate[ax][ay])
    print(ax + 1, ay + 1) 
else:
    print(0)


'''
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 1 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 1
1 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 2
1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 2 2 0 0 0 0 0 0 0 0 0 0 0 0
1 0 1 1 0 1 1 2 1 1 1 1 1 1 1 0 0 0 0
1 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 1 0 0 0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 2 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 2 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 2 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 2 0 0 2 2
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 2 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 2
0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 1 2 2 2
0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 2 2 2

답: 15 4
'''