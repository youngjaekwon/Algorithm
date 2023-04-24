def solution(dartResult):
    skip = -1
    res = []
    for i, x in enumerate(dartResult):
        if i == skip:
            continue
        if i < len(dartResult) - 1 and x == "1" and dartResult[i+1] == "0":
            x = "10"
            skip = i + 1

        if x.isnumeric():
            res.append(int(x))
        elif x in ["D", "T"]:
            res[-1] **= 2 if x == "D" else 3
        elif x == "*":
            if len(res) > 1:
                res[-2] *= 2
                res[-1] *= 2
            else:
                res[-1] *= 2
        elif x == "#":
            res[-1] *= -1

    return sum(res)