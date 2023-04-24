def solution(a, b):
    if a == b:
        return a
    l = sorted([a, b])
    return sum(range(l[0], l[1] + 1))