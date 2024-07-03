t = int(input())

def dfs(x):
    global answer
    q = []
    q.append(x)
    visited[x] = 1

    for i in graph[x]:
        if visited[i] == 0:
            answer += 1
            dfs(i)


for _ in range(t):
    n, m = map(int,input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    answer = 0
    for _ in range(m):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)


    dfs(1)

    print(answer)
