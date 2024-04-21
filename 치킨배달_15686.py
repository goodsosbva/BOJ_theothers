from itertools import combinations

n, m = map(int, input().split())
chickens = []
houses = []

for i in range(n):
    for j, val in enumerate(map(int, input().split())):
        if val == 1:
            houses.append((i, j))
        elif val == 2:
            chickens.append((i, j))


def caculate_disc(cor1, cor2):
    x1, y1 = cor1
    x2, y2 = cor2

    chickens_dist = abs(x1 - x2) + abs(y1 - y2)
    return chickens_dist

ans = 2 * n * len(houses)
for comb in combinations(chickens, m):
    candi = 0
    for house in houses:
        candi += min(caculate_disc(house, chicken) for chicken in chickens)
    
    ans = min(candi, ans)

print(ans)