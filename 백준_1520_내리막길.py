n, m = map(int, input().split())
maps = [[*map(int, input().split())] for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if maps[x][y] > maps[nx][ny]:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]


print(dfs(0, 0))



