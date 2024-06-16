n = int(input())
arr = [0]  
for _ in range(n):
    arr.append(int(input()))

visited = [False] * (n + 1)
answer = set()

def dfs(start, current, path):
    if current in path:
        if start == current:
            answer.update(path)
        return
    if visited[current]:
        return
    
    visited[current] = True
    path.add(current)
    dfs(start, arr[current], path)
    path.remove(current)
    visited[current] = False


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, i, set())

print(len(answer))
for num in sorted(answer):
    print(num)
