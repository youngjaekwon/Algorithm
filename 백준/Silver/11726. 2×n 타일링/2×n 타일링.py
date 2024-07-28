N = int(input())

memoization = [1, 2]

for i in range(2, N):
    memoization.append((memoization[i - 1] + memoization[i - 2]) % 10007)

print(memoization[N - 1])