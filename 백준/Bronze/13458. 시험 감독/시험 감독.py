from math import ceil

N = int(input())
A = list(map(int, input().split()))
B, C = list(map(int, input().split()))

cnt = 0

for i in range(N):
    A[i] -= B
    cnt += 1
    if A[i] > 0:
        cnt += ceil(A[i] / C)

print(cnt)