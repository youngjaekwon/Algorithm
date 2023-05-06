N, M = list(map(int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0


def melt(MAP):
    melted_MAP = [[0 for _ in range(M)] for _ in range(N)]
    for i, line in enumerate(MAP):
        for j, x in enumerate(line):
            if x == 0:
                continue
            else:
                n = 0
                for di, dj in zip(dx, dy):
                    ni = i + di
                    nj = j + dj
                    if ni < 0 or ni >= N or nj < 0 or nj >= M or MAP[ni][nj] != 0:
                        continue
                    n += 1
                melted_MAP[i][j] = max(MAP[i][j] - n, 0)

    return melted_MAP


def dfs(start, MAP):
    x, y = start
    queue = [(x, y)]
    MAP[x][y] = 0

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or MAP[nx][ny] == 0:
                continue

            MAP[nx][ny] = 0
            queue.append((nx, ny))

    return MAP


year = 0
while True:
    year += 1
    MAP = melt(MAP)

    break_check = max(map(max, MAP))

    if not break_check:
        break

    count = 0
    MAP_COPY = [list(line) for line in MAP]

    while True:
        for i, line in enumerate(MAP_COPY):
            for j, x in enumerate(line):
                if x > 0:
                    MAP_COPY = dfs((i, j), MAP_COPY)
                    count += 1
                    break
            else:
                continue
            break
        else:
            break

    if count > 1:
        answer = year
        break

print(answer)