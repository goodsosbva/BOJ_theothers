n = int(input())


def find_middle_values(sorted_list):
    n = len(sorted_list)
    mid_index = n // 2
    if n % 2 == 0:
        return sorted_list[mid_index - 1], sorted_list[mid_index]
    else:
        return sorted_list[mid_index]


cordsx = []
cordsy = []
cords = []
for _ in range(n):
    x, y = map(int, input().split())
    cordsx.append(x)
    cordsy.append(y)
    cords.append([x, y])


sorted_cordsx = sorted(cordsx)
sorted_cordsy = sorted(cordsy)

if n % 2 != 0:
    answer = 0
    ax = find_middle_values(sorted_cordsx)
    ay = find_middle_values(sorted_cordsy)

    for i in range(n):
        answer += abs(cords[i][0] - ax) + abs(cords[i][1] - ay)

    print(answer)

else:
    ans1 = 0
    ans2 = 0
    ax1, ax2 = find_middle_values(sorted_cordsx)
    ay1, ay2 = find_middle_values(sorted_cordsy)

    for i in range(n):
        ans1 += abs(cords[i][0] - ax1) + abs(cords[i][1] - ay1)
        ans2 += abs(cords[i][0] - ax2) + abs(cords[i][1] - ay2)

    print(min(ans1, ans2))






# 5
# 2 2
# 3 4
# 5 6
# 1 9
# -2 -8