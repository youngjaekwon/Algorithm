def solution(t, p):
    x = -len(p) + 1 or None
    l = []
    for i, _ in list(enumerate(t[:x])):
        y = int(t[i:i+len(p)])

        if y <= int(p):
            l.append(y)
    return len(l)