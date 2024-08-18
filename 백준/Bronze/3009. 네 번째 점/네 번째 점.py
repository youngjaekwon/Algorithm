x1 = 0
x2 = 0
y1 = 0
y2 = 0
answer = [0, 0]
for _ in range(3):
    x, y = list(map(int, input().split()))
    if x1 == 0:
        x1 = x
    elif x1 != x:
        if x2 == 0:
            x2 = x
        else:
            answer[0] = 1
    else:
        answer[0] = 2
    if y1 == 0:
        y1 = y
    elif y1 != y:
        if y2 == 0:
            y2 = y
        else:
            answer[1] = 1
    else:
        answer[1] = 2

if answer[0] == 1:
    answer[0] = x1
else:
    answer[0] = x2
if answer[1] == 1:
    answer[1] = y1
else:
    answer[1] = y2

print(answer[0], answer[1])