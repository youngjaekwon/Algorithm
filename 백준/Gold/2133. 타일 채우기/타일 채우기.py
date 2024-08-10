N = int(input())
memoization = [1]

for i in range(1, N + 1):
    if i % 2 == 1:
        memoization.append(0)
        continue
    num = memoization[i - 2] * 3
    num2 = 0
    if i > 3:
        for j in range(0, i - 3, 2):
            num2 += memoization[j]
    num += num2 * 2
    memoization.append(num)

print(memoization[N])