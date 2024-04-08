from collections import defaultdict

n, d, k, c = map(int, input().split())

sushis = []
for i in range(n):
    s = int(input())
    sushis.append(s)

l = 0
r = k - 1
sushisCount = defaultdict(int)

sushisCount[c] += 1
for i in range(k):
    sushisCount[sushis[i]] += 1


answer = -1
while l < n:
    isMax = len(sushisCount)
    answer = max(isMax, answer)

    sushisCount[sushis[l]] -= 1
    if sushisCount[sushis[l]] == 0:
        del sushisCount[sushis[l]]

    l += 1
    r += 1

    sushisCount[sushis[r % n]] += 1

print(answer)
    