import sys
sys.setrecursionlimit(200000)

n, r, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

subtree_size = [0] * (n + 1)
visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    subtree_size[node] = 1 

    for neighbor in graph[node]:
        if not visited[neighbor]:
            subtree_size[node] += dfs(neighbor)
    
    return subtree_size[node]

dfs(r)

queries = [int(input()) for _ in range(q)]
results = [subtree_size[query] for query in queries]

for result in results:
    print(result)
