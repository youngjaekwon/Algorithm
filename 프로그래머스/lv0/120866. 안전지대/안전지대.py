def solution(board):
    res = [list(li) for li in board]
    ln = len(board) - 1
    
    if not ln:
        return 0 if board[0][0] == 1 else 1

    for i, row in enumerate(board):
        for j, v in enumerate(row):
            if v == 1:
                if ln > i > 0 and ln > j > 0:
                    res[i - 1][j - 1:j + 2] = [1, 1, 1]
                    res[i][j - 1:j + 2] = [1, 1, 1]
                    res[i + 1][j - 1:j + 2] = [1, 1, 1]
                elif (i == 0 and j == 0) :
                    res[i][j:j + 2] = [1, 1]
                    res[i + 1][j:j + 2] = [1, 1]
                elif (i == 0 and j == ln) :
                    res[i][j - 1:j + 1] = [1, 1]
                    res[i + 1][j - 1:j + 1] = [1, 1]
                elif (i == ln and j == 0) :
                    res[i - 1][j:j + 2] = [1, 1]
                    res[i][j:j + 2] = [1, 1]                    
                elif (i == ln and j == ln) :
                    res[i - 1][j - 1:j + 1] = [1, 1]
                    res[i][j - 1:j + 1] = [1, 1]
                elif j == 0:
                    res[i - 1][j:j + 2] = [1, 1]
                    res[i][j:j + 2] = [1, 1]
                    res[i + 1][j:j + 2] = [1, 1]
                elif j == ln:
                    res[i - 1][j - 1:j + 1] = [1, 1]
                    res[i][j - 1:j + 1] = [1, 1]
                    res[i + 1][j - 1:j + 1] = [1, 1]
                elif i == 0:
                    res[i][j - 1:j + 2] = [1, 1, 1]
                    res[i + 1][j - 1:j + 2] = [1, 1, 1]
                elif i == ln:
                    res[i - 1][j - 1:j + 2] = [1, 1, 1]
                    res[i][j - 1:j + 2] = [1, 1, 1]

    return len([i for li in res for i in li if i == 0])