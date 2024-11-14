seq = input()
de = input()
en = input()
ls = len(seq)

dp = [[0] * len(seq) for _ in range(2)]

for i, (d, e) in enumerate(zip(de, en)):
    dp_copy = [list(d) for d in dp]
    for j, c in enumerate(seq):
        if d == c:
            if j == 0:
                dp_copy[0][0] += 1
            else:
                dp_copy[0][j] += dp[1][j - 1]
        if e == c:
            if j == 0:
                dp_copy[1][0] += 1
            else:
                dp_copy[1][j] += dp[0][j - 1]
    dp = dp_copy

print(dp[0][-1] + dp[1][-1])