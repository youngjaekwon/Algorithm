import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark = 2
eated = 0
shark_location = None

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_location = (i, j)


def find_nearest(start):
    """
    가장 가까운 물고기를 찾는다
    """
    min_distance = float("inf")
    nearest = []

    q = deque([(0, *start)])
    visited = {start}

    while q:
        count, x, y = q.popleft()
        if (x, y) != start and 0 < board[x][y] < shark:
            if count < min_distance:
                min_distance = count
                nearest = [(x, y)]
            elif count == min_distance:
                nearest.append((x, y))
        if count >= min_distance:
            continue

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < N
                and 0 <= ny < N
                and (nx, ny) not in visited
                and board[nx][ny] <= shark
            ):
                q.append((count + 1, nx, ny))
                visited.add((nx, ny))

    if nearest:
        return sorted(nearest)[0], min_distance
    else:
        return None, None


def eat(nearest):
    """
    물고기를 먹는다
    """
    global shark
    global shark_location
    global eated
    x, y = nearest
    eated += 1
    if shark == eated:
        shark += 1
        eated = 0
    board[shark_location[0]][shark_location[1]] = 0
    board[x][y] = 9
    shark_location = (x, y)


count = 0

while True:
    nearest, distance = find_nearest(shark_location)
    if nearest is None:
        break
    eat(nearest)
    count += distance

print(count)
