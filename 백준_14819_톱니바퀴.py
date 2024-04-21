Gears = []
for _ in range(4):
    gear = input()
    input_list = [int(bit) for bit in gear]
    Gears.append(input_list)

north = [0] * 4
next_move = []
k = int(input())

for _ in range(k):
    move, direction = map(int, input().split())
    
    move -= 1
    next_move = [[move, 0]]

    # 해당 움직인 톱니 바퀴를 기준으로 왼쪽, 오른쪽 이동
    for i in range(move + 1, 4):
        if Gears[i - 1][(north[i - 1] + 2) % 8] != Gears[i][(north[i] + 6) % 8]:
            next_move.append([i, (i - move) % 2])
        else:
            break
    
    for i in range(move - 1, -1, -1):
        if Gears[i][(north[i] + 2) % 8] != Gears[i + 1][(north[i + 1] + 6) % 8]:
            next_move.append([i, (move - i) % 2])
        else:
            break

    for i, dir in next_move:
        if dir == 0:
            north[i] = (north[i] - direction + 8) % 8
        else:
            north[i] = (north[i] + direction + 8) % 8


total = 0
start = 1
for i in range(0, 4):
    if Gears[i][north[i]] == 1:
        total += start
    
    start *= 2

print(total)
# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1
