W, L = list(map(int, input().split()))
N = int(input())
stores = [list(map(int, input().split())) for _ in range(N)]
dk = list(map(int, input().split()))


def f(dk, s):
    if dk[0] == 1:
        if s[0] == 1:
            return abs(dk[1] - s[1])
        elif s[0] == 2:
            d1 = L + dk[1] + s[1]
            d2 = L + (W - dk[1]) + (W - s[1])
            return min([d1, d2])
        elif s[0] == 3:
            return dk[1] + s[1]
        else:
            return (W - dk[1]) + s[1]
    elif dk[0] == 2:
        if s[0] == 1:
            d1 = L + dk[1] + s[1]
            d2 = L + (W - dk[1]) + (W - s[1])
            return min([d1, d2])
        elif s[0] == 2:
            return abs(dk[1] - s[1])
        elif s[0] == 3:
            return dk[1] + (L - s[1])
        else:
            return (W - dk[1]) + (L - s[1])
    elif dk[0] == 3:
        if s[0] == 1:
            return dk[1] + s[1]
        elif s[0] == 2:
            return s[1] + (L - dk[1])
        elif s[0] == 3:
            return abs(dk[1] - s[1])
        else:
            d1 = dk[1] + W + s[1]
            d2 = (L - dk[1]) + W + (L - s[1])
            return min([d1, d2])
    else:
        if s[0] == 1:
            return (W - s[1]) + dk[1]
        elif s[0] == 2:
            return (W - s[1]) + (L - dk[1])
        elif s[0] == 3:
            d1 = dk[1] + W + s[1]
            d2 = (L - dk[1]) + W + (L - s[1])
            return min([d1, d2])
        else:
            return abs(dk[1] - s[1])


answer = 0

for store in stores:
    answer += f(dk, store)

print(answer)
