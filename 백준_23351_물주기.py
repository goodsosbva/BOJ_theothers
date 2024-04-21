n, k, a, b = map(int, input().split())

lifes = []

def deathChk(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            return True
    return False

def SearchFirstMinLife(arr):
    minLifeValue = min(arr)
    for i in range(len(arr)):
        if arr[i] == minLifeValue:
            return i

for _ in range(n):
    lifes.append(k)

answer = 0

while deathChk(lifes) != True:
    PlusLifeStarIdx = SearchFirstMinLife(lifes)

    for i in range(PlusLifeStarIdx, PlusLifeStarIdx + a):

        lifes[i % len(lifes)] += b

    for i in range(len(lifes)):
        lifes[i] -= 1
    answer += 1

print(answer)
