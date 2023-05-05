N = int(input())
MAP = [list(input()) for _ in range(N)]
DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]
result = []

while True:
    x, y = 0, 0
    for i, line in enumerate(MAP):
        con = True
        for j, n in enumerate(line):
            if n == "1":
                x, y = i, j
                con = False
                break
        if not con:
            break
    else:
        break

    visited = set()
    queue = [(x, y)]
    MAP[x][y] = "0"

    while queue:
        x, y = queue.pop(0)
        visited.add((x, y))

        for dx, dy in zip(DX, DY):
            nx = x + dx
            ny = y + dy

            if (
                nx < 0
                or nx >= N
                or ny < 0
                or ny >= N
                or MAP[nx][ny] == "0"
                or (nx, ny) in visited
            ):
                continue
            MAP[nx][ny] = "0"
            queue.append((nx, ny))

    result.append(len(visited))

print(len(result))

result.sort()

for num in result:
    print(num)