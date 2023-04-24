def solution(name, yearning, photo):
    d = dict([(n, yearning[i]) for i, n in enumerate(name)])
    return [sum([d[n] if n in d else 0 for n in p]) for p in photo]