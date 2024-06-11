import copy
from collections import deque

n = int(input())

maps = []
maxCount = -1
minCount = 101
answer = -1
for _ in range(n):
    mp = list(map(int, input().split()))
    isMax = max(mp)
    isMin = min(mp)
    maxCount = max(maxCount, isMax)
    minCount = min(minCount, isMin)
    maps.append(mp)


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque([])
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isRetangle(nx, ny) and copyed_maps[nx][ny] == 1 and chk[nx][ny] == -1:
                chk[nx][ny] = 1
                q.append([nx, ny])

def isRetangle(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


for h in range(0, 1):
    chk = [[-1 for j in range(n)] for i in range(n)]
    copyed_maps = copy.deepcopy(maps)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if copyed_maps[i][j] > h:
                copyed_maps[i][j] = 1
            else:
                copyed_maps[i][j] = -1

    for i in range(n):
        for j in range(n):
            if chk[i][j] == -1 and copyed_maps[i][j] == 1:
                bfs(i, j)
                cnt += 1
    answer = max(answer, cnt)


for h in range(minCount, maxCount):
    chk = [[-1 for j in range(n)] for i in range(n)]
    copyed_maps = copy.deepcopy(maps)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if copyed_maps[i][j] > h:
                copyed_maps[i][j] = 1
            else:
                copyed_maps[i][j] = -1

    for i in range(n):
        for j in range(n):
            if chk[i][j] == -1 and copyed_maps[i][j] == 1:
                bfs(i, j)
                cnt += 1
    answer = max(answer, cnt)

print(answer)

