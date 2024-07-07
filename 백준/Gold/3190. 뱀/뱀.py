from typing import Deque
from collections import deque

N = int(input())
K = int(input())
apples = {tuple(map(int, input().split())) for _ in range(K)}
L = int(input())
commands = [list(input().split()) for _ in range(L)]
commands = [(int(t), c) for t, c in commands]


def create_arr() -> list[list[int]]:
    tmp = []
    for i in range(N):
        row = []
        for j in range(N):
            val = 0
            if (i + 1, j + 1) in apples:
                val = 1
            row.append(val)
        tmp.append(row)
    return tmp


arr = create_arr()


class Snake:
    body: Deque[tuple[int, int]]

    def __init__(self) -> None:
        self.body = deque()
        self.body.append((0, 0))

    def move(self, dx: int, dy: int) -> int:
        xp, yp = self.body[0][0] + dx, self.body[0][1] + dy

        if xp == -1 or xp == N or yp == -1 or yp == N or (xp, yp) in self.body:
            return -1

        self.body.appendleft((xp, yp))

        n = arr[xp][yp]

        if not n:
            self.body.pop()
        else:
            arr[xp][yp] = 0

        return 0


snake = Snake()
# 좌상우하
x_arr = [0, -1, 0, 1]
y_arr = [-1, 0, 1, 0]
d = 2
next_command = 0
time = 0

while True:
    if next_command != -1 and commands[next_command][0] == time:
        command = commands[next_command][1]
        next_command += 1
        if next_command == len(commands):
            next_command = -1

        if command == "L":
            d -= 1
            if d == -1:
                d = 3
        elif command == "D":
            d += 1
            if d == 4:
                d = 0

    time += 1

    result = snake.move(x_arr[d], y_arr[d])

    if result == -1:
        break

print(time)
