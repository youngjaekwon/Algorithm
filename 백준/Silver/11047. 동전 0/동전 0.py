N, K = list(map(int, input().split()))
arr = [int(input()) for _ in range(N)]

answer = 0

for c in reversed(arr):
    if c == 0:
        break
    if c > K:
        continue
    answer += K // c
    K = K % c

print(answer)
