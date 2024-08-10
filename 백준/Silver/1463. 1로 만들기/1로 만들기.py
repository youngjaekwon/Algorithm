from collections import deque

N = int(input())

queue = deque([(0, N)])
answer = 0

while True:
    c, x = queue.popleft()
    if x == 1:
        answer = c
        break

    c += 1

    if x % 3 == 0:
        queue.append((c, x // 3))
    if x % 2 == 0:
        queue.append((c, x // 2))
    queue.append((c, x - 1))

print(answer)