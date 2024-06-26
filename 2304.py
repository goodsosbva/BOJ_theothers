n = int(input())

coordi = [0] * 1001
answer = 0

maxHeight = -1
maxIdx = -1
for i in range(n):
    x, y = map(int, input().split())
    coordi[x] = y

    if maxHeight < y:
        maxHeight = y
        maxIdx = x

curValue = 0
for i in range(maxIdx + 1):
    curValue = max(coordi[i], curValue)
    answer += curValue

curValue = 0
for i in range(1000, maxIdx, -1):
    curValue = max(coordi[i], curValue)
    answer += curValue

print(answer)

# 3
# 0 3
# 1 2
# 2 3
# 답 9
#

# 4
# 1 3
# 2 2
# 3 3
# 4 3
# 답 12


# 5
# 4 3
# 6 5
# 9 5
# 11 3
# 13 4
# 답 42