from collections import deque

F, S, G, U, D = list(map(int, input().split()))

visited = [False for _ in range(F + 1)]
queue = deque([(0, S)])
count = -1

while queue:
    cnt, floor = queue.popleft()

    if floor == G:
        count = cnt
        break

    if (uf := floor + U) <= F and not visited[uf]:
        visited[uf] = True
        queue.append((cnt + 1, uf))
    if (df := floor - D) > 0 and not visited[df]:
        visited[df] = True
        queue.append((cnt + 1, df))

if count != -1:
    print(count)
else:
    print("use the stairs")