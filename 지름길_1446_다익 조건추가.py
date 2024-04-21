import math

max_float = math.inf
n, d = map(int , input().split(" "))
shortcuts = []
graph = [[] for _ in range(d + 1)]
visited = [False] * (d + 1)
distance = [max_float] * (d + 1)

for i in range(d):
    graph[i].append((i + 1, 1))

for i in range(n):
    pleaseContinue = False
    start, end, dis = map(int, input().split())
    if start < 0 or end > d:
        continue
    
    for w in graph[start]:
        a, b = w
        if a == end and b < dis:
            pleaseContinue = True
            break
    
    if pleaseContinue:
        continue

    graph[start].append((end, dis))


def getSmallestNode():
    index = 0
    minValue = math.inf
    for i in range(1, d + 1):
        if not visited[i] and distance[i] < minValue:
            minValue = distance[i]
            index = i

    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    for k in graph[start]:
        distance[k[0]] = k[1]

    for _ in range(d - 1):
        daum = getSmallestNode()
        visited[daum] = True

        for q in graph[daum]:
       

            cost = distance[daum] + q[1]
            if cost < distance[q[0]]:
                if q[1] > distance[q[0]] - distance[daum]:
                    continue
                distance[q[0]] = cost

dijkstra(0)
print(distance[d])


"""
2 10000
0 10000 9999
1 9999 1
"""

"""
2 20
0 10 5
2 7 3
"""

"""
4 150
0 50 10
50 100 10
100 151 10
110 140 90
"""