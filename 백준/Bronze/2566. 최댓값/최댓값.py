N = 9
board = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
result = (0, 0)

for i, line in enumerate(board):
    for j, num in enumerate(line):
        if num >= MAX:
            MAX = num
            result = i + 1, j + 1

print(MAX)
print(" ".join(map(str, result)))