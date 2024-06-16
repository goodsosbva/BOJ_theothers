n = int(input())
nodes = [0]
for _ in range(n):
    nodes.append(int(input()))


visited = [-1] * (n + 1)
answer = set()


def dfs(start, current, path):
    if current in path:
        if current == start:
            answer.update(path)
        return
    
    if visited[current] == 1:
        return
    
    visited[current] = 1
    path.add(current)
    dfs(start, nodes[current], path)
    visited[current] = -1
    path.remove(current)


for i in range(1, n + 1):
    if visited[i] == -1:
        dfs(i, i, set())


print(len(answer))
for a in sorted(answer):
    print(a)