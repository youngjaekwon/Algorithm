def move(key, player):
    if key == "up":
        return [player[0], player[1] + 1]
    elif key == "down":
        return [player[0], player[1] - 1]
    elif key == "left":
        return [player[0] - 1, player[1]]
    else:
        return [player[0] + 1, player[1]]

def solution(keyinput, board):
    answer = []
    player = [0, 0]

    for key in keyinput:
        tmp = move(key, player)
        if abs(tmp[0]) > board[0] // 2 or abs(tmp[1]) > board[1] // 2:
            continue
        else:
            player = tmp

    return player