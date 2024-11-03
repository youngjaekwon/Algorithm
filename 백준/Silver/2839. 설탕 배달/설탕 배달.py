N = int(input())

dp = [0, 0, 0, 1, 0, 1]
if N > 5:
    for i in range(6, N + 1):
        dp_i = 0
        if dp[i - 5]:
            dp_i = dp[i - 5] + 1
        elif dp[i - 3]:
            dp_i = dp[i - 3] + 1

        dp.append(dp_i)

print(dp[N] if dp[N] else -1)
