# def calculateInclination(x, y):
#     return x / y
#
#
# tc = int(input())
# for _ in range(tc):
#     n = int(input())
#     dic = {}
#     answer = 0
#
#     if n == 0:
#         print(answer)
#         continue
#
#     for x in range(1, n + 1):
#         for y in range(1, n + 1):
#             inclination = calculateInclination(x, y)
#
#             if inclination in dic:
#                 continue
#             else:
#                 dic[inclination] = 1
#                 answer += 1
#
#     print(answer +  2)
#
def computePhiUpToN(n):
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i

    return phi


def uniqueInclinations(n):
    phiValues = computePhiUpToN(n)
    totalInclinations = sum(phiValues)
    return totalInclinations * 2 + 1


tc = int(input())
for _ in range(tc):
    n = int(input())

    answer = uniqueInclinations(n)
    print(answer)

