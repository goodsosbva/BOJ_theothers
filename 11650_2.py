import sys

N = int(sys.stdin.readline())
num = dict()

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())

    if x not in num:
        print("x!=y")
        num[x] = [y]
    else:
        print("x==y")
        num[x].append(y)
    print(num)
print("start")
for v in num.values():
    v.sort()
num = sorted(num.items())

for i in num:
    for j in i[1]:
        print(i[0], j)