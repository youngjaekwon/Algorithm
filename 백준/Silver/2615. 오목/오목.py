arr = [list(map(int, input().split())) for _ in range(19)]

"""
[아래, 우측, 우측아래, 좌측아래]
"""
x_arr = [1, 0, 1, 1]
y_arr = [0, 1, 1, -1]
searched = set()


def search(c: int, x: int, y: int) -> tuple[bool, tuple[int, int] | None]:
    for d in range(4):
        cnt = 1
        xp, yp = x, y
        fxp, fyp = 0, 0
        for i in range(6):
            xp, yp = xp + x_arr[d], yp + y_arr[d]
            if xp == 19 or yp == 19 or arr[xp][yp] != c or (xp, yp, d) in searched:
                break
            cnt += 1
            fxp, fyp = xp, yp
            searched.add((xp, yp, d))

        if cnt == 5:
            return True, (x, y) if d != 3 else (fxp, fyp)

    return False, None


result = []
p = []

for i in range(19):
    for j in range(19):
        v = arr[i][j]
        if not v:
            continue
        r, rp = search(v, i, j)
        if r:
            result.append(v)
            p.append((rp[0] + 1, rp[1] + 1))

if len(result) == 1:
    print(result[0])
    print(p[0][0], p[0][1])
else:
    print(0)
