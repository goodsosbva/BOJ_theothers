from collections import deque

def bfs(x, y, maps, chk):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque([(x, y)])
    chk[x][y] = 1  

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1 and chk[nx][ny] == -1:
                q.append((nx, ny))
                chk[nx][ny] = 1

tc = int(input())

for _ in range(tc):
    m, n, k = map(int, input().split())

    maps = [[0 for _ in range(m)] for _ in range(n)]
    chk = [[-1 for _ in range(m)] for _ in range(n)]
    answer = 0

    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1
        
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and chk[i][j] == -1:
                bfs(i, j, maps, chk)
                answer += 1

    print(answer)
