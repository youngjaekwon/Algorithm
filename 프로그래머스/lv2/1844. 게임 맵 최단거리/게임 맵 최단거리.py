from collections import deque

def solution(maps):
    queue = deque([(0, 0, 1)])
    r = len(maps)
    c = len(maps[0])
    visited = [[False] * c for _ in range(r)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, distance = queue.popleft()

        if x == r - 1 and y == c - 1:
            return distance

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < r
                and 0 <= ny < c
                and not visited[nx][ny]
                and maps[nx][ny] == 1
            ):
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))

    return -1