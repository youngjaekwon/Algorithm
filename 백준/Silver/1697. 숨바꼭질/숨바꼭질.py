from collections import deque

N, K = list(map(int, input().split()))

queue = deque([(0, N)])
visited = [False for _ in range(100001)]

while queue:
    cnt, n = queue.popleft()
    if n == K:
        print(cnt)
        break

    n1 = n - 1
    n2 = n + 1
    n3 = 2 * n
    if n > 0 and not visited[n1]:
        visited[n1] = True
        queue.append((cnt + 1, n1))
    if n2 <= 100000 and not visited[n2]:
        visited[n2] = True
        queue.append((cnt + 1, n2))
    if n3 <= 100000 and not visited[n3]:
        visited[n3] = True
        queue.append((cnt + 1, n3))