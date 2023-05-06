t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    M = [list(map(int, input().split())) for _ in range(n + 2)]
    home_x, home_y = M.pop(0)
    penta_x, penta_y = M[-1]

    queue = [(home_x, home_y)]
    result = "sad"
    visited = set(queue)

    while queue:
        x, y = queue.pop()
        if penta_x == x and penta_y == y:
            result = "happy"
            break

        for i, j in M:
            if abs(i - x) + abs(j - y) <= 1000 and (i, j) not in visited:
                visited.add((i, j))
                queue.append((i, j))

    answer.append(result)

for r in answer:
    print(r)