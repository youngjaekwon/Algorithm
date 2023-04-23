N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

answer = list(range(1, N + 1))

for x, y in board:
    x -= 1
    y -= 1
    answer[x], answer[y] = answer[y], answer[x]

print(" ".join(map(str, answer)))