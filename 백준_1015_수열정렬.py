n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    b.append([a[i], i])

b.sort()

ps = [-1] * n

for j in range(len(b)):
    value, index = b[j]
    ps[index] = j

for p in ps:
    print(p, end=' ')




