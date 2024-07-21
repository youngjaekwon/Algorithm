T = int(input())
arr = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def solution():
    M, N, K = map(int, input().split())
    cabs = [tuple(map(int, input().split())) for _ in range(K)]

    visited = set()
    count = 0

    for i in range(N):
        for j in range(M):
            if (j, i) in cabs and (i, j) not in visited:
                count += 1
                queue = [(i, j)]
                visited.add((i, j))
                while queue:
                    x, y = queue.pop(0)
                    for dx, dy in arr:
                        xp, yp = x + dx, y + dy
                        if (
                            not (0 <= xp < N and 0 <= yp < M)
                            or not (yp, xp) in cabs
                            or (xp, yp) in visited
                        ):
                            continue
                        queue.append((xp, yp))
                        visited.add((xp, yp))

    print(count)


for _ in range(T):
    solution()
