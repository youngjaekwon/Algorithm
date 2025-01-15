N, M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
PR, PC = list(map(int, input().split()))
PR, PC = PR - 1, PC - 1

"""
0 1 2 3
상 하 좌 우
"""
direction = 0
darr = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def fun1():
    global direction
    if direction == 0:
        direction = 2
    elif direction == 1:
        direction = 3
    elif direction == 2:
        direction = 0
    elif direction == 3:
        direction = 1


def fun2():
    global direction
    if direction == 0:
        direction = 3
    elif direction == 1:
        direction = 2
    elif direction == 2:
        direction = 1
    elif direction == 3:
        direction = 0


def cal():
    global direction
    t = 1
    pr, pc = PR, PC
    visited = set([(pr, pc, direction)])

    while True:
        pr, pc = pr + darr[direction][0], pc + darr[direction][1]
        if not (0 <= pr < N and 0 <= pc < M):
            break
        elif (pr, pc, direction) in visited:
            t = -1
            break
        visited.add((pr, pc, direction))
        t += 1
        b = board[pr][pc]
        if b == "\\":
            fun1()
        elif b == "/":
            fun2()
        elif b == "C":
            t -= 1
            break

    return t


answer = -1
answer_direction = ""

for i, d in [
    (0, "U"),
    (3, "R"),
    (1, "D"),
    (2, "L"),
]:
    direction = i
    res = cal()
    if res == -1:
        print(d)
        print("Voyager")
        break
    elif res > answer:
        answer_direction = d
        answer = res
else:
    print(answer_direction)
    print(answer)
