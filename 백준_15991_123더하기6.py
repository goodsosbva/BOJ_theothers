t = int(input())

dp = [0] * 100001
dp[0], dp[1], dp[2], dp[3], dp[4], dp[5], dp[6] = 1, 1, 2, 2, 3, 3, 6
for i in range(7, 100001):
    dp[i] = (dp[i - 6] + dp[i - 4] + dp[i - 2]) % 1000000009

for _ in range(t):
    n = int(input())
    print(dp[n])

