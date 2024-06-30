n = int(input())

dices = []
for _ in range(n):
    dice = list(map(int, input().split()))
    dices.append(dice)

opposite_index = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0,
}

answer = 0

for i in range(6):
    base_index = i
    base = dices[0][base_index]
    top_index = opposite_index[base_index]
    top = dices[0][top_index]
    ans = 0

    for k in range(6):
        if k != base_index and k != top_index:
            ans = max(ans, dices[0][k])

    for j in range(1, n):
        for k in range(6):
            if dices[j][k] == top:
                base_index = k
                top_index = opposite_index[base_index]
                base = dices[j][base_index]
                top = dices[j][top_index]
                break

        max_side = 0
        for k in range(6):
            if k != base_index and k != top_index:
                max_side = max(max_side, dices[j][k])
        ans += max_side

    answer = max(answer, ans)

print(answer)
