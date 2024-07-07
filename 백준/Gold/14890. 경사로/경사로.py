N, L = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

# 우하
x_arr = [0, 1]
y_arr = [1, 0]


def check(x: int, y: int, d: int) -> int:
    cnt = 1
    prev = arr[x][y]
    ramps = set()
    p = 0  # or 1 or 2, neutral, up, down

    while True:
        x, y = x + x_arr[d], y + y_arr[d]
        if x == N or y == N:
            return 1 if p != 2 or cnt >= L else 0
        current = arr[x][y]

        if current == prev:
            cnt += 1
            if p == 2 and cnt == L:
                p = 0
                for i in range(L):
                    point = (x - x_arr[d] * i, y - y_arr[d] * i)
                    if point in ramps:
                        return 0
                    ramps.add(point)
        elif current > prev:
            if current - 1 > prev:
                return 0
            if p == 2 and cnt == 1:
                return 0

            if cnt >= L:
                p = 0
                for i in range(L):
                    point = (x - x_arr[d] * (i + 1), y - y_arr[d] * (i + 1))
                    if point in ramps:
                        return 0
                    ramps.add(point)
            else:
                return 0
            p = 1
            cnt = 1
        elif current < prev:
            if current + 1 < prev:
                return 0
            if p == 2:
                if cnt >= L:
                    p = 0
                    for i in range(L):
                        point = (x - x_arr[d] * i, y - y_arr[d] * i)
                        if point in ramps:
                            return 0
                        ramps.add(point)
                else:
                    return 0
            p = 2
            cnt = 1

        prev = current


answer = 0

for i in range(N):
    answer += check(i, 0, 0)
    answer += check(0, i, 1)

print(answer)
