def solution(N, number):
    dp = [{N}, {int(f"{N}{N}"), N + N, N - N, N * N, N // N}]

    for i, l in enumerate(dp):
        if number in l:
            return i + 1

    x = 2
    answer = -1
    while x < 9:
        x += 1
        l = {int(f"{N}" * x)}

        for i in range(x - 1):
            for a in dp[i]:
                for b in dp[x - i - 2]:
                    l.add(a + b)
                    l.add(a - b)
                    l.add(a * b)
                    if b:
                        l.add(a // b)

        if number in l:
            answer = x
            break

        dp.append(l)

    return answer