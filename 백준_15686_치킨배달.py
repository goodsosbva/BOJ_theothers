from itertools import combinations

n, m = map(int, input().split())
houses = []
chickens = []

for i in range(n):
    for j, val in enumerate(map(int, input().split())):
        if val == 1:
            houses.append((i, j))

        elif val == 2:
            chickens.append((i, j))


def calulate_dist(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    return abs(x1 - x2) + abs(y1 - y2)

ans = 2 * n * len(houses)
for comb in combinations(chickens, m):
    candi = 0
    for house in houses:
        candi += min(calulate_dist(house, chicken) for chicken in comb)

    ans = min(ans, candi)

print(ans)

