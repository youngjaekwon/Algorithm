def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    while True:
        burst = []
        for i, row in enumerate(board[:-1]):
            for j, item in enumerate(row[:-1]):
                if item == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != "X":
                    burst.extend([(i, j), (i, j+1), (i+1, j),(i+1, j+1)])
        burst = set(burst)
        if burst:
            for x, y in sorted(burst):
                for i in range(x-1, -1, -1):
                    if (z:=board[i][y]) != "X":
                        board[i+1][y] = z
                        board[i][y] = "X"
            answer += len(burst)
        else:
            break

    return answer