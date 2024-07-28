T = int(input())

for _ in range(T):
    memoization = [1, 2, 4, 7]
    n = int(input())

    for i in range(4, n):
        memoization.append(memoization[i - 1] + memoization[i - 2] + memoization[i - 3])

    print(memoization[n - 1])