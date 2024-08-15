N, A, B = list(map(int, input().split()))
arr = sorted(
    [list(map(int, input().split())) for _ in range(N)], key=lambda t: t[0] - t[1]
)

answer = 0

for i in range(A):
    answer += arr[i][0]

for i in range(A, N):
    answer += arr[i][1]

print(answer)