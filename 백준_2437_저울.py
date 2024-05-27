n = int(input())
weights = list(map(int, input().split()))
cur_weight = 0

weights.sort()
for i in range(len(weights)):
    if weights[i] > cur_weight + 1:
        break
    elif weights[i] <= cur_weight + 1:
        cur_weight += weights[i]

print(cur_weight + 1)