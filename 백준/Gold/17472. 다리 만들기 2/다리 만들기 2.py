from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]

visited = set()
count = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and (i, j) not in visited:
            q = deque()
            q.append((i, j))
            visited.add((i, j))
            board[i][j] = count
            while q:
                y, x = q.popleft()
                for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    ny, nx = y + dy, x + dx
                    if (
                        0 <= ny < N
                        and 0 <= nx < M
                        and board[ny][nx] == 1
                        and (ny, nx) not in visited
                    ):
                        q.append((ny, nx))
                        board[ny][nx] = count
                        visited.add((ny, nx))
            count += 1


parents = list(range(count))


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


edges = []

for i in range(N):
    start = 0
    end = 0
    distance = 0
    for j in range(M):
        x = board[i][j]
        if start == 0:
            start = x
        else:
            if x == 0:
                distance += 1
            elif x != start:
                end = x
            else:
                distance = 0
        if end != 0:
            if distance > 1:
                edges.append((distance, start, end))
            start = x
            end = 0
            distance = 0

for i in range(M):
    start = 0
    end = 0
    distance = 0
    for j in range(N):
        x = board[j][i]
        if start == 0:
            start = x
        else:
            if x == 0:
                distance += 1
            elif x != start:
                end = x
            else:
                distance = 0
        if end != 0:
            if distance > 1:
                edges.append((distance, start, end))
            start = x
            end = 0
            distance = 0

edges.sort()

answer = 0
connected = 0
for distance, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += distance
        connected += 1


print(answer if connected == count - 2 else -1)
