N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MAP = [[0] * 100 for _ in range(100)]

for x, y in board:
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            MAP[i][j] = 1

print(sum([sum(line) for line in MAP]))