from collections import Counter

def solution(lines):
    l = list()
    for line in lines:
        l.extend(range(line[0], line[1]))
    c = Counter(l)
    res = [i for i, v in c.items() if v > 1]
    return len(res)