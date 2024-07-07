import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

graph = [[] for _ in range(n + 1)]
weights = [0] * (n + 1)
realWeights = [0] * (n + 1)

for _ in range(n - 1):
    x, y, w = map(int, input().split())
    graph[x].append([y, w])
    graph[y].append([x, w])

def dfs(node, innerWeights):
    for next, w in graph[node]:
        if innerWeights[next] == 0:
            innerWeights[next] = w + innerWeights[node]
            dfs(next, innerWeights)

dfs(1, weights)
weights[1] = 0

maxIndex = weights.index(max(weights))

dfs(maxIndex, realWeights)
realWeights[maxIndex] = 0

print(max(realWeights))
