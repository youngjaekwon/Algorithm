def solution(emergency):
    d1 = dict()
    for i in emergency:
        d1[i] = 0
    sorted_e = sorted(emergency, reverse=True)
    for i, v in enumerate(sorted_e):
        d1[v] = i + 1
    return list(d1.values())