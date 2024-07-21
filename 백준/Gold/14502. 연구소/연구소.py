from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
arr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

zeros = []

for i in range(N):
    for j in range(M):
        if not board[i][j]:
            zeros.append((i, j))

cases = combinations(zeros, 3)
results = []

for case in cases:
    board_copy = [list(row) for row in board]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                queue = [(i, j)]
                visited = set(queue)
                while queue:
                    x, y = queue.pop(0)
                    for dx, dy in arr:
                        xp, yp = x + dx, y + dy
                        if (
                            not (0 <= xp < N and 0 <= yp < M)
                            or (xp, yp) in case
                            or board[xp][yp] == 1
                            or (xp, yp) in visited
                        ):
                            continue
                        board_copy[xp][yp] = 2
                        queue.append((xp, yp))
                        visited.add((xp, yp))

    results.append(sum([row.count(0) for row in board_copy]) - 3)


print(max(results))
