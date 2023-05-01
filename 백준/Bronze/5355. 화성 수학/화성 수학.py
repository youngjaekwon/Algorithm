N = int(input())
board = [list(input().split()) for _ in range(N)]

for line in board:
    num = float(line[0])
    for x in line[1:]:
        if x == "@":
            num *= 3
        elif x == "%":
            num += 5
        elif x == "#":
            num -= 7
    print(f"{num:.2f}")