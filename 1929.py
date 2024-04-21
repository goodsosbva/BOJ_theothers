n, k = map(int, input().split())

primenums = []

for num in range(n, k):
    dividedCount = 0
    if num == 1:
        continue
    for i in range(2, num + 1):
        if num % i == 0:
            dividedCount += 1
    if dividedCount == 1:
        primenums.append(num)

#  print(primenums)
for i in primenums:
    print(i)