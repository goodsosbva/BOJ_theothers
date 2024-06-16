import sys
sys.setrecursionlimit(10000) 

n, c, k = map(int, input().split())
ais = list(map(int, input().split()))
indexing_ais = list(enumerate(ais, start=1))
sorted_indexing_ais = sorted(indexing_ais, key=lambda x: x[1])

visited = [0 for _ in range(n + 1)]
maps = [[0] * (n + 1) for _ in range(n + 1)]
node_list = []

for _ in range(c):
    x, y = map(int, input().split())
    maps[x][y] = 1
    maps[y][x] = 1

def dfs(num):
    visited[num] = 1
    node_list.append(num)
    for i in range(1, n + 1):
        if visited[i] == 0 and maps[num][i] == 1:
            dfs(i)

answer = 0
for st, money in sorted_indexing_ais:
    if visited[st] == 0 and k >= money:
        dfs(st)
        k -= money
        answer += money
unique_nodes = len(set(node_list))

if unique_nodes == n:
    print(answer)
else:
    print('Oh no')
