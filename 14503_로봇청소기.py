n, m = map(int, input().split())
x, y, direct = map(int, input().split())

dx = [-1, 0, 1, 0, -1, 0, 1, 0]
dy = [0, 1, 0, -1, 0, 1, 0, -1]

maps = []
answer = 1
for i in range(n):
    singleMap = list(map(int, input().split()))
    maps.append(singleMap)

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1


def print_maps(arr):
    for a in arr:
        print(a)


while True:
    flag = 0
    for i in range(4):
        nx = x + dx[(direct + 3) % 4]
        ny = y + dy[(direct + 3) % 4]
        direct = (direct + 3) % 4
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                answer += 1
                y = ny
                x = nx
                flag = 1
                break

    # 후진 상황
    if flag == 0:
        if maps[x - dx[direct]][y - dy[direct]] == 1:
            print(answer)
            break
        else:
            y, x = y - dy[direct], x - dx[direct]

