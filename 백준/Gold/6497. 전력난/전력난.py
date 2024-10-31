import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def solution():
    m, n = list(map(int, input().split()))
    if m == 0 and n == 0:
        return 0

    max_costs = 0
    edges = []
    for _ in range(n):
        x, y, z = list(map(int, input().split()))
        edges.append((z, x, y))
        max_costs += z

    edges.sort()

    parents = list(range(m + 1))

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
    print(max_costs - answer)
    return 1


if __name__ == "__main__":
    while True:
        res = solution()
        if not res:
            break
