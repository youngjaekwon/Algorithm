def solution(n, control):
    d = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10
    }
    return n + sum(map(d.get, control))