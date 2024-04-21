tc = int(input())


def chkSameLength(l, r, lengths):
    while l <= r:
        m = (l + r) // 2
        if coordinate[m] == lengths:
            return True
        elif coordinate[m] > lengths:
            r = m - 1
        else:
            l = m + 1
    return False


for _ in range(tc):
    k = int(input())
    coordinate = list(map(int, input().split()))
    n = len(coordinate)
    l, r = 0, n - 1
    answer = 0
    coordinate.sort()

    for a in range(n - 1):
        for b in range(a + 1, n):
            lengths = abs(coordinate[b] - coordinate[a])

            if chkSameLength(l, r, lengths + coordinate[b]) == True:
                answer += 1

    print(answer)
