N, M = map(int, input().split())
board1 = [list(map(int, input().split())) for _ in range(N)]
board2 = [list(map(int, input().split())) for _ in range(N)]

[
    print(" ".join([str(x + y) for x, y in zip(line1, line2)]))
    for line1, line2 in zip(board1, board2)
]