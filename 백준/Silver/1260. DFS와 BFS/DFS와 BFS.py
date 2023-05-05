NODE, EDGE, START = list(map(int, input().split()))
M = [list(map(int, input().split())) for _ in range(EDGE)]

DFS = []
stack = [START]

while stack:
    node = stack.pop()
    if node in DFS:
        continue
    DFS.append(node)

    l = list()

    for A, B in M:
        if A == node:
            l.append(B)
        elif B == node:
            l.append(A)

    stack.extend((sorted(l, key=lambda x: -x)))

BFS = []
queue = [START]

while queue:
    node = queue.pop(0)
    if node in BFS:
        continue
    BFS.append(node)

    l = []
    for A, B in M:
        if A == node and B not in BFS:
            l.append(B)
        elif B == node and A not in BFS:
            l.append(A)
    queue.extend(sorted(l))

print(" ".join(map(str, DFS)))
print(" ".join(map(str, BFS)))