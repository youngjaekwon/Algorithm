import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = list(map(int, input().split()))

nodes = [list(map(int, input().split())) for _ in range(N)]
edges = [(0, *list(map(int, input().split()))) for _ in range(M)]

for i, a in enumerate(nodes):
    for j, b in enumerate(nodes):
        if i != j:
            distance = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
            edges.append((distance, i + 1, j + 1))

edges.sort()

parents = list(range(N + 1))


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


answer = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(f"{answer:.2f}")
