def greatestCommonFactor(a, b):
    if b == 0:
        return a

    return greatestCommonFactor(b, a % b)


def lowestCommonMultiple(a, b, gcd):
    a = a / gcd
    b = b / gcd
    lcm = a * b * gcd

    return lcm


k = int(input())
commons = []

#print(commons)
for _ in range(k):
    commons = list(map(int, input().split()))
    gcdAllPlus, gcd = 0, 0
    for j in range(1, len(commons) - 1):
        for k in range(j + 1, len(commons)):
        # if commons[j] != commons[k]:
            #print(commons[j])
            #print(commons[k])
            gcd = greatestCommonFactor(commons[j], commons[k])
        # while commons[k]: commons[j], commons[k] = commons[k], commons[j] % commons[k]
        # gcd = commons[j]
            gcdAllPlus += gcd

    print(gcdAllPlus)

