N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
answer = [0] * N
for i, j, k in board:
    answer[i - 1 : j] = [k] * (j - i + 1)

print(" ".join(map(str, answer)))