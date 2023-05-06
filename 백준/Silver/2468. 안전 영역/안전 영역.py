N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

S, E = min(map(min, MAP)), max(map(max, MAP))

answer = set([1])

for D in range(S, E + 1):
    count = 0
    MAP_COPY = [list(line) for line in MAP]
    for i, line in enumerate(MAP_COPY):
        for j, num in enumerate(line):
            if num > D:
                queue = [(i, j)]
                MAP_COPY[i][j] = D

                while queue:
                    x, y = queue.pop(0)

                    for _x, _y in zip(dx, dy):
                        nx, ny = x + _x, y + _y
                        if (
                            nx < 0
                            or nx >= N
                            or ny < 0
                            or ny >= N
                            or MAP_COPY[nx][ny] <= D
                        ):
                            continue
                        MAP_COPY[nx][ny] = D
                        queue.append((nx, ny))
                count += 1

    answer.add(count)

print(max(answer))