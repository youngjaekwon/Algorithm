import sys, heapq

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    start, end = list(map(int, input().split()))
    heapq.heappush(arr, (start, 1))
    heapq.heappush(arr, (end, -1))

room = 0
answer = 0

for _ in range(N * 2):
    _, v = heapq.heappop(arr)
    room += v
    answer = max(answer, room)

print(answer)