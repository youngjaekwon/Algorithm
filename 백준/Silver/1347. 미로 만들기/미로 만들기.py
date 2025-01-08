_ = int(input())
command = input()

board = [["."]]

"""
direction
0 1 2 3
하 우 상 좌
"""

direction = 0
x, y = 0, 0


def extend(d):
    global board

    if d == 0:
        new_line = ["#" for _ in board[-1]]
        board.append(new_line)
    elif d == 1:
        for line in board:
            line.append("#")
    elif d == 2:
        new_line = [["#" for _ in board[0]]]
        board = new_line + board
    else:
        new_board = []
        for line in board:
            new_line = ["#"] + line
            new_board.append(new_line)
        board = new_board


def move():
    global board
    global direction
    global y
    global x

    d = direction % 4
    if d == 0:
        y += 1
        if y >= len(board):
            extend(d)
    elif d == 1:
        x += 1
        if x >= len(board[y]):
            extend(d)
    elif d == 2:
        y -= 1
        if y < 0:
            extend(d)
            y += 1
    else:
        x -= 1
        if x < 0:
            extend(d)
            x += 1
    board[y][x] = "."


for c in command:
    if c == "R":
        direction -= 1
    elif c == "L":
        direction += 1
    else:
        move()


for l in board:
    print("".join(l))