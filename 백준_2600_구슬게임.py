bs = list(map(int, input().split()))

dp = [[-1] * 501 for _ in range(501)]

def whoWin(k1, k2):
    if dp[k1][k2] != -1:
        return dp[k1][k2]
    
    for b in bs:
        if b <= k1 and not whoWin(k1 - b, k2):
            dp[k1][k2] = 1
            return dp[k1][k2]
        if b <= k2 and not whoWin(k1, k2 - b):
            dp[k1][k2] = 1
            return dp[k1][k2]
        
    dp[k1][k2] = 0
    return dp[k1][k2]


for _ in range(5):
    k1, k2 = map(int, input().split())

    if whoWin(k1, k2):
        print('A')
    else:
        print('B')