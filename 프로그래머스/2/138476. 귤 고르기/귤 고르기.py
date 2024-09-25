from collections import deque

def solution(k, tangerine):
    cases = dict()
    for t in tangerine:
        if t not in cases:
            cases[t] = 1
        else:
            cases[t] += 1
    total = len(tangerine)
    diff = total - k
    nt = deque(sorted(cases.items(), key=lambda t: t[1]))

    while diff:
        t, c = nt.popleft()
        if c > diff:
            nt.appendleft((t, c))
            break
        diff -= c
    
    return len(nt)