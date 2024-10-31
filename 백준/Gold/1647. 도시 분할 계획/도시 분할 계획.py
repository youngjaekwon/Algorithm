import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = list(map(int, input().split()))

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


edges = []
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    edges.append((c, a, b))
edges.sort()


answer = 0
max_edge = 0
for cost, a, b in edges:
    if find(a) != find(b):
        answer += cost
        union(a, b)
        max_edge = cost

answer -= max_edge
print(answer)
