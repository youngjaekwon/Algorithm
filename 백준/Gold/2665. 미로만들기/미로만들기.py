n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
x_arr = [-1, 1, 0, 0]
y_arr = [0, 0, -1, 1]

queue = [(0, 0, 0)]
count = None
visited = {(0, 0)}

while queue:
    queue.sort(key=lambda tp: tp[0])
    c, x, y = queue.pop(0)
    if x == n - 1 and y == n - 1:
        count = c
        break

    for i in range(4):
        dx, dy = x_arr[i], y_arr[i]
        xp, yp = x + dx, y + dy
        if xp == -1 or xp == n or yp == -1 or yp == n:
            continue
        if (xp, yp) not in visited:
            cp = c + int(not bool(arr[xp][yp]))
            queue.append((cp, xp, yp))
            visited.add((xp, yp))


print(count)
