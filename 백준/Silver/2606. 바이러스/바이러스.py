N = int(input())
CON = int(input())
M = [list(map(int, input().split())) for _ in range(CON)]

queue = [1]
visited = set()

while queue:
    pc = queue.pop(0)
    visited.add(pc)
    for A, B in M:
        if A == pc and B not in visited:
            queue.append(B)
        elif B == pc and A not in visited:
            queue.append(A)

print(len(visited) - 1)