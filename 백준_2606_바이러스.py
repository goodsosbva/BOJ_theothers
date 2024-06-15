n = int(input())
connects = int(input())

connectList = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
answer = 0
for _ in range(connects):
    a, b = map(int, input().split())

    connectList[a][b] = 1
    connectList[b][a] = 1


def dfs(num):
    global answer
    visited[num] = 1
    answer += 1
    for i in range(n + 1):
        if visited[i] == 0 and connectList[num][i] == 1:
            dfs(i)


dfs(1)
print(answer - 1)