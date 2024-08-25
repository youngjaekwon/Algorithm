N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))

if K >= N:
    print(0)
else:
    points = []
    for i in range(N - 1):
        points.append((arr[i + 1] - arr[i], i + 1))
    points.sort(reverse=True)

    groups = []
    start = 0
    for _, i in sorted(points[: K - 1], key=lambda t: t[1]):
        groups.append(arr[start:i])
        start = i
    groups.append(arr[start:N])

    answer = sum(group[-1] - group[0] for group in groups)
    print(answer)