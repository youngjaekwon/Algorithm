N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

answer = list(range(1, N + 1))

for begin, end, mid in board:
    begin -= 1
    mid -= 1
    end -= 1
    answer[begin : end + 1] = answer[mid : end + 1] + answer[begin:mid]

print(" ".join(map(str, answer)))