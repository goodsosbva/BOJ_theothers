n = int(input())

numbers = list(map(int, input().split()))

prefixSum = []
init = 0
for n in numbers:
    if (n == 1):
        init += 1
        prefixSum.append(init)
    else:
        init += -1
        prefixSum.append(init)


prefixMax = 0
prefixMin = 0
answer = 0
for i in range(len(numbers)):
    if prefixSum[i] > prefixMax:
        prefixMax = prefixSum[i]
    elif prefixSum[i] < prefixMin:
        prefixMin = prefixSum[i]

    print(prefixMax, prefixMin)

    answer = max(answer, abs(prefixSum[i] - prefixMin))
    answer = max(answer, abs(prefixSum[i] - prefixMax))

print(answer)

# 10
# 1 2 1 1 2 2 2 2 2 1
# 5
