def solution():
    k = int(input())
    n = int(input())

    dp = [[i + 1 for i in range(n)]]

    for i in range(1, k + 1):
        u = dp[i - 1]
        tmp = []
        for j in range(n):
            tmp.append(sum(u[: j + 1]))
        dp.append(tmp)

    print(dp[-1][-1])


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        solution()
