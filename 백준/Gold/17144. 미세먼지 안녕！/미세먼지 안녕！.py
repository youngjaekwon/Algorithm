R, C, T = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(R)]

# 상하좌우
arr_x = [-1, 1, 0, 0]
arr_y = [0, 0, -1, 1]


def copy_arr():
    tmp = []
    for row in arr:
        tmp.append(list(row))
    return tmp


def diffuse():
    zero_points = set()
    copied_arr = copy_arr()

    for i in range(R):
        for j in range(C):
            if arr[i][j] == 0:
                zero_points.add((i, j))

    for i in range(R):
        for j in range(C):
            if (i, j) not in zero_points and arr[i][j] > 0:
                val = arr[i][j] // 5
                cnt = 0
                for k in range(4):
                    xp = i + arr_x[k]
                    yp = j + arr_y[k]
                    if xp == -1 or xp == R or yp == -1 or yp == C:
                        continue
                    elif arr[xp][yp] == -1:
                        continue
                    copied_arr[xp][yp] += val
                    cnt += 1
                copied_arr[i][j] -= val * cnt

    return copied_arr


class Filter:
    top: tuple[int, int]
    bottom: tuple[int, int]

    def __init__(self):
        tmp_x, tmp_y = 0, 0
        for i in range(R):
            is_break = False
            for j in range(C):
                if arr[i][j] == -1:
                    tmp_x, tmp_y = i, j
                    is_break = True
                    break
            if is_break:
                break

        self.top = (tmp_x, tmp_y)
        self.bottom = (tmp_x + 1, tmp_y)

    def clean(self, bt: str, s_list: list[int], x: int, y: int):
        s_index = 0  # 진행방향 인덱스
        while True:
            p = arr[x][y]
            s = s_list[s_index]
            if s == s_list[-1] and p == -1:
                break
            xp = x + arr_x[s]
            yp = y + arr_y[s]
            if (
                xp == -1
                or xp == R
                or yp == -1
                or yp == C
                or (bt == "top" and p != -1 and xp == self.top[0] + 1)
                or (bt == "bottom" and p != -1 and xp == self.bottom[0] - 1)
            ):
                s_index += 1
                continue
            n = arr[xp][yp]
            if n == -1 and p != -1:
                arr[x][y] = 0
            elif p != -1:
                arr[x][y] = n
            x, y = xp, yp

    def clean_top(self) -> None:
        s_list = [0, 3, 1, 2]  # 상우하좌
        self.clean("top", s_list, *self.top)

    def clean_bottom(self) -> None:
        s_list = [1, 3, 0, 2]  # 하우상좌
        self.clean("bottom", s_list, *self.bottom)


f = Filter()

for _ in range(T):
    arr = diffuse()
    f.clean_top()
    f.clean_bottom()

res = 0
for row in arr:
    res += sum(row)

print(res + 2)
