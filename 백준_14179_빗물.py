h, w = map(int, input().split())

blocks = list(map(int, input().split()))

answer = 0
leftHeight = [0] * w
rightHeight = [0] * w

leftHeight[0] = blocks[0]
for i in range(1, w):
    leftHeight[i] = max(leftHeight[i - 1], blocks[i])

rightHeight[-1] = blocks[-1]
for j in range(w - 2, -1, -1):
    rightHeight[j] = max(rightHeight[j + 1], blocks[j])

for k in range(w):
    answer += min(leftHeight[k], rightHeight[k]) - blocks[k]

print(answer)
