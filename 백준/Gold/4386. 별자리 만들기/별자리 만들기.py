import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

edges = []
for i, a in enumerate(stars):
    for j, b in enumerate(stars):
        if i != j:
            distance = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
            edges.append((distance, i, j))

edges.sort()

parents = list(range(n))


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
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost

print(f"{answer:.2f}")
