n, m = map(int, input().split())

k = int(input())
graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
distance = [99999] * (n + 1)

for i in range(n + 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def getSmallestNode():
    minValue = 99999
    index = 0
    for i in range(1, n + 1):
        if not visited[i] and distance[i] < minValue:
            minValue = distance[i]
            index = i

    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = 0

    for j in graph[start]:
        distance[j[0]] = j[1]


    for _ in range(n - 1):
        now = getSmallestNode()
        visited[now] = True

        for k in graph[now]:
            cost = distance[now] + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost


dijkstra(k)
print(distance)


"""
5 6
1
5 1 1
1 2 1
1 3 3
2 3 1
2 4 5
3 4 2
"""