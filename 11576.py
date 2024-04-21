n, k = map(int, input().split())
positionNum = int(input())
before = list(map(int, input().split()))

t = 0
print(before)

for i in range(positionNum):
    t += before[-1] * (n ** i)
    before.pop(-1)
    print(before)
    print(t)
#print(before)

after = []
while t > 0:
    after.append(str(t % k))
    t //= k

print(' '.join(after[::-1]))
