n = int(input())

#nums = []
primenums = []

nums = list(map(int, input().split()))
#for i in int(input()):
    #k = int(input())
    #nums.append(k)

for j in nums:
    dividedCount = 0
    if j == 1:
        continue
    for i in range(2, j + 1):
        if j % i == 0:
            dividedCount += 1
    if dividedCount == 1:
        primenums.append(j)

#  print(' '.join(primenums[::-1]))
print(len(primenums))
