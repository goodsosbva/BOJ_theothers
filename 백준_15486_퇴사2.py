n = int(input())

dp = [0] * (n + 1)
works = [[0, 0]]
for _ in range(1, n + 1):
    t, p = map(int, input().split())
    works.append([t, p])

for i in range(1, len(works)):
    t, p = works[i]
    dp[i] = max(dp[i], dp[i - 1])
    if i + t - 1 <= n:
        dp[i + t - 1] = max(dp[i - 1] + p, dp[i + t - 1])

print(dp[-1])