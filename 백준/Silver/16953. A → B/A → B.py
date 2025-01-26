A, B = list(map(int, input().split()))


def f1(n):
    return n // 2


def f2(n):
    return int(n[:-1]) if len(n) > 1 else 0


c = 1

while True:
    if B % 2:
        sb = str(B)
        if sb[-1] != "1":
            c = -1
            break
        B = f2(sb)
    else:
        B = f1(B)
    c += 1
    if B == A:
        break
    elif B < A:
        c = -1
        break

print(c)
