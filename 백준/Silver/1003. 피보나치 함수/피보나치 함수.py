T = int(input())

dp = [(1, 0), (0, 1), (1, 1), (1, 2), (2, 3), (3, 5)]

for i in range(6, 41):
    a = dp[i - 1]
    b = dp[i - 2]
    dp.append((a[0] + b[0], a[1] + b[1]))

for _ in range(T):
    N = int(input())
    print(*dp[N])
