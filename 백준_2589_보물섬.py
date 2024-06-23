from collections import deque

n, m = map(int, input().split())

max_map = [[-1 for _ in range(m)] for _ in range(n)]
maps = []

for _ in range(n):
    mp = input()
    maps.append(list(mp))


def bfs(x, y, chk, cnt, maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append([x, y])
    chk[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isRetangle(nx, ny) and chk[nx][ny] == 0 and maps[nx][ny] == 'L':
                chk[nx][ny] = chk[x][y] + 1
                cnt = max(cnt, chk[nx][ny])
                q.append([nx, ny])

    return cnt - 1            


def isRetangle(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


for y in range(m):
    for x in range(n):
        if maps[x][y] == 'L' and max_map[x][y] == -1:
            chk = [[0 for _ in range(m)] for _ in range(n)]
            cnt = 0
            max_cnt = bfs(x, y, chk, cnt, maps)
            max_map[x][y] = max_cnt

answer = 0
for max_mp in max_map:
    answer = max(answer, max(max_mp))

print(answer)
# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW