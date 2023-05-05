from collections import deque

N, M = list(map(int, input().split()))
MAP = [list(input()) for _ in range(N)]
DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

queue = deque([(1, 0, 0)])

while queue:
    c, x, y = queue.popleft()
    if x == N - 1 and y == M - 1:
        print(c)
        break

    for dx, dy in zip(DX, DY):
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M or MAP[nx][ny] == "0":
            continue
        MAP[nx][ny] = "0"
        queue.append((c + 1, nx, ny))