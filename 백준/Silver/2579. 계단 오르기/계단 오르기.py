N = int(input())

stairs = [[(0, 0)]]
for i in range(1, N + 1):
    n = int(input())
    tmp = []
    tmp_jumped = []
    tmp_continued = []
    if i > 1:
        for c, v in stairs[i - 2]:
            tmp_jumped.append((1, v + n))
    for c, v in stairs[i - 1]:
        if c < 2:
            tmp_continued.append((c + 1, v + n))
    if tmp_jumped:
        tmp_jumped.sort(key=lambda t: t[1])
        tmp.append(tmp_jumped[-1])
    tmp_continued.sort(key=lambda t: t[1])
    tmp.append(tmp_continued[-1])
    stairs.append(tmp)

answer = max(t[1] for t in stairs[-1])
print(answer)
