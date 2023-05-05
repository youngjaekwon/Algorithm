n = int(input())
x, y = list(map(int, input().split()))
m = int(input())

M = [list(map(int, input().split())) for _ in range(m)]

queue = [(0, x)]
count = -1
visited = set()

while queue:
    cnt, node = queue.pop(0)
    if node == y:
        count = cnt
        break
    visited.add(node)

    for a, b in M:
        if a == node and b not in visited:
            queue.append((cnt + 1, b))
        elif b == node and a not in visited:
            queue.append((cnt + 1, a))

print(count)