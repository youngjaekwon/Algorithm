def solution(sides):
    t = []
    for i in range(1, sum(sides) + 1):
        tmp = sides + [i]
        mx = max(tmp)
        tmp.remove(mx)
        if mx < sum(tmp):
            t.append(i)
    return len(t)