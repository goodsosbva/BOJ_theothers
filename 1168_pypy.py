import sys

input = sys.stdin.readline


def update(i, diff):
    while i < size:
        bit[i] += diff
        i |= i + 1


def get(x):  # size = 4
    left, right = 0, size
    for i in range(exp + 1):
        mid = (left + right) >> 1
        val = bit[mid - 1]
        if val >= x:
            right = mid
        else:
            left = mid
            x -= val
    return left


n, k = map(int, input().split())

exp, size = 0, 1
while size < n:
    exp += 1
    size *= 2
bit = [0] * size
for i in range(n):
    update(i, 1)



ans = []
x = 0
for j in range(n, 0, -1):
    x = (x + k - 1) % j

    val = get(x + 1)
    update(val, -1)
    ans.append(val + 1)

sys.stdout.write(f'<{", ".join(map(str, ans))}>')