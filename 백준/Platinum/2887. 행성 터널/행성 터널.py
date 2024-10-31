N = int(input())

planets = []
for i in range(N):
    x, y, z = tuple(map(int, input().split()))
    planets.append((x, y, z, i + 1))

edges = []


def update_edges(idx):
    for i, a in enumerate(planets[:-1]):
        b = planets[i + 1]
        distance = abs(a[idx] - b[idx])
        edges.append((distance, a[3], b[3]))


planets.sort(key=lambda p: p[0])
update_edges(0)
planets.sort(key=lambda p: p[1])
update_edges(1)
planets.sort(key=lambda p: p[2])
update_edges(2)
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
for distance, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += distance

print(answer)
