N = 5
board = [list(input()) for _ in range(N)]
answer = ""
end = 0
while board_copy := [line for line in board if line]:
    for line in board_copy:
        answer += line.pop(0)
print(answer)