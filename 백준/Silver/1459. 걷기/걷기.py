X, Y, W, S = list(map(int, input().split()))

count = 0
d = min(X, Y)
if W * 2 < S:
    count += d * W * 2
    X -= d
    Y -= d
    count += max(X, Y) * W
else:
    count += d * S
    X -= d
    Y -= d
    r = max(X, Y)
    if S < W:
        if r % 2 == 0:
            count += r * S
        else:
            count += (r - 1) * S + W
    else:
        count += r * W

print(count)