import heapq
import sys

input = sys.stdin.readline

N, M, K = list(map(int, input().split()))
beers = sorted([tuple(map(int, input().split())) for _ in range(K)], key=lambda x: x[1])


class Beer(object):
    def __init__(self, v, c):
        self.v = v
        self.c = c

    def __repr__(self):
        return f"Beer v: {self.v}, c: {self.c}"

    def __lt__(self, other):
        return self.v < other.v


beers = [Beer(v, c) for v, c in beers]


answers = []
min_heap = []
s = 0

for beer in beers:
    heapq.heappush(min_heap, beer)
    s += beer.v

    if len(min_heap) > N:
        min_beer = heapq.heappop(min_heap)
        s -= min_beer.v

    if s >= M and len(min_heap) == N:
        answers.append(beer.c)

if answers:
    print(min(answers))
else:
    print(-1)
