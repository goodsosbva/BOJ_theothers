import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(i):
    subtree_size[i] = 1

    for next in graph[i]:
        if subtree_size[next] == 0:
            subtree_size[i] += dfs(next)
    
    return subtree_size[i]

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

subtree_size = [0] * (n + 1)

dfs(r)

for _ in range(q):
    qu = int(input())
    print(subtree_size[qu])