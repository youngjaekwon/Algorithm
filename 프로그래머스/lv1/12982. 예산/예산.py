def solution(d, budget):
    d = sorted(d)
    a = 0
    for i in d:
        if i > budget:
            break
        budget -= i
        a += 1
    return a