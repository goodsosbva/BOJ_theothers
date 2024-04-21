N, M = map(int, input().split())
#n = int(input())

def countNumber(n, m):
    cnt = 0
    k = 1
    u = n
    while u > k:
        cnt = cnt + n // (m * k)
        #print("n:", n, end=" ")
        k *= m
    #print("\n")
    return cnt

fiveCount = countNumber(N, 5) - countNumber(M, 5) - countNumber(N - M, 5)
twoCount = countNumber(N, 2) - countNumber(M, 2) - countNumber(N - M, 2)

ans = min(fiveCount, twoCount)
print(ans)