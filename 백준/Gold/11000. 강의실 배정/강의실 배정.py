N = int(input())
arr = []

for _ in range(N):
    start, end = list(map(int, input().split()))
    arr.append((start, 1))
    arr.append((end, -1))

arr.sort()

room = 0
answer = 0

for _, v in arr:
    room += v
    answer = max(answer, room)

print(answer)