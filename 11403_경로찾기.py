n = int(input())

graph = []
# i -> j: 0 or 1
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            # j -> i and i -> k => j -> k
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for g in graph:
    print(*g)
