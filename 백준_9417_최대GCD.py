def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

tc = int(input())
for _ in range(tc):
    numbers = list(map(int, input().split()))

    gcdList = []
    for a in range(len(numbers)):
        for b in range(a + 1, len(numbers)):
            gcdNumber = gcd(numbers[a], numbers[b])
            gcdList.append(gcdNumber)

    print(max(gcdList))
