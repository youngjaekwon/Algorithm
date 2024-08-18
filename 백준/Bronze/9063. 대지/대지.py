N = int(input())
xarr = []
yarr = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    xarr.append(x)
    yarr.append(y)

print((max(xarr) - min(xarr)) * (max(yarr) - min(yarr)))