N = int(input())
memoization = [-1]

for i in range(1, N + 1):
    counts = []
    if i % 3 == 0:
        counts.append(memoization[i // 3])
    if i % 2 == 0:
        counts.append(memoization[i // 2])
    counts.append(memoization[i - 1])
    memoization.append(min(counts) + 1)

print(memoization[-1])