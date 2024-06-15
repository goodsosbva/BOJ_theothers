n = int(input())
start, end = map(int, input().split())
c = int(input())


connectList = [[0] * (n + 1) for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]
answer = 10001
cnt = 0
for _ in range(c):
    x, y = map(int, input().split())

    connectList[x][y] = 1
    connectList[y][x] = 1


def dfs(num, cnt):
    global answer

    visited[num] = 1

    if num == end:
        answer = min(answer, cnt)
        return answer 
    for i in range(n + 1):
        if visited[i] == -1 and connectList[num][i] == 1:
            dfs(i, cnt + 1)

dfs(start, cnt)

if answer == 10001:
    print(-1)
else:
    print(answer)