from collections import Counter

def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    res = list()
    only_zero = True
    for i, v in x.items():
        if i in y:
            if i != "0":
                only_zero = False
            res.extend(i * min(v, y[i]))
    if not res:
        return "-1"
    elif only_zero:
        return "0"
    else:
        return "".join(sorted(res, key=lambda x: int(x), reverse=True))