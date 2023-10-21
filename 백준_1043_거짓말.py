n, m = map(int, input().split())

knows = list(map(int, input().split()))
trueer = []
answer = 0

length = knows[0]

for i in range(1, length + 1):
    trueer.append(knows[i])

partys = []
for _ in range(m):
    party = list(map(int, input().split()))
    partys.append(party[1:])

for _ in range(m):
    for humans in partys:
        for h in humans:
            if h in trueer:
                trueer.extend(humans)
                break

partys = [set(humans) for humans in partys]
trueer = set(trueer)
for humans in partys:
    if humans & trueer:
        continue
    answer += 1

print(answer)

     
"""
4 5
1 1
1 1
1 2
1 3
1 4
2 4 1

2

6 5
1 6
2 4 5
2 1 2
2 2 3
2 3 4
2 5 6

0
"""

# 다른 사람 코드  (유니 파인드)

import sys
input = sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]

# 사실을 아는 사람과 Union시, 해당 사람이 부모노드가 되도록
def union(parent, a, b, know_truth):
    a = find(parent, a)
    b = find(parent, b)

    if a in know_truth and b in know_truth:
        return

    if a in know_truth:
        parent[b] = a
    
    elif b in know_truth:
        parent[a] = b
    
    else:
        if a < b:
            parent[b] = a
        
        else:
            parent[a] = b


n, m = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]

parties = []
parent = list(range(n+1))

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]
    
    for i in range(party_len - 1):
        union(parent, party[i], party[i+1], know_truth)
    
    parties.append(party)
    
ans = 0
for party in parties:
    for i in range(len(party)):
        if find(parent, party[i]) in know_truth:
            break
    
    else:
        ans += 1

print(ans)
