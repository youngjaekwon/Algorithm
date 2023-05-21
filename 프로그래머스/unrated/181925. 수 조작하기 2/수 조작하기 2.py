def solution(numLog):
    d = {1: "w", -1: "s", 10: "d", -10: "a"}
    return "".join([d.get(numLog[i + 1] - v) for i, v in enumerate(numLog[:-1])])