from itertools import combinations


n, d = map(int , input().split(" "))
optimumDistance = 10001
shortcuts = []
for i in range(n):
    start, end, distance = map(int, input().split())
    if start < 0 or end > d:
        continue
    
    shortcuts.append([start, end, distance])


for i in range(1, len(shortcuts) + 1):
    perms = list(combinations(shortcuts, i))
    for perm in perms:
        # perm은 튜플의 리스트이므로, 각 튜플을 리스트로 변환
        perm_as_list = [list(item) for item in perm]
        perm_as_list.sort()

        cur = 0
        distance = 0
        while cur < d:
            if len(perm_as_list) > 0:
                if cur == perm_as_list[0][0]:
                    distance += perm_as_list[0][2]
                    cur += (perm_as_list[0][1] - perm_as_list[0][0])
                    perm_as_list.pop(0)
                
                else:
                    distance += 1
                    cur += 1
            else:
                distance += 1
                cur += 1
                
        optimumDistance = min(optimumDistance, distance)
print(optimumDistance)






"""
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90 
답: 70
"""